
from fastapi import FastAPI, Depends, Request, Response
from fastapi.responses import RedirectResponse, JSONResponse
from gateway.api_router import call_api_gateway, RedirectProbationerPortalException, RedirectJobVacancyPortalException, RedirectLibraryOccasionPortalException
from controller import erp
from probationer_sub import probationer_main
from jobvacancy_sub import jobvacancy_main
from library_sub import library_main

from loguru import logger
from uuid import uuid4

app = FastAPI()
app.include_router (erp.router, 
                    dependencies=[Depends(call_api_gateway)], prefix='/probation')
logger.add("info.log",format="Log: [{extra[log_id]}: {time} - {level} - {message} ", level="INFO", enqueue = True)

@app.middleware("http")
async def log_middleware(request:Request, call_next):
    
    log_id = str(uuid4())
    with logger.contextualize(log_id=log_id):
        logger.info('Request to access ' + request.url.path)
        try:
            response = await call_next(request)
        except Exception as ex: 
            logger.error(f"Request to " + request.url.path + " failed: {ex}")
            response = JSONResponse(content={"success": False}, status_code=500)
        finally: 
            logger.info('Successfully accessed ' + request.url.path)
            return response

@app.exception_handler(RedirectProbationerPortalException)
def exception_handler_probationer(request: Request, exc: RedirectProbationerPortalException) -> Response:
    return RedirectResponse(url='http://localhost:8000/probation/probationer/index')
  
@app.exception_handler(RedirectJobVacancyPortalException)
def exception_handler_jobvacancy(request: Request, exc: RedirectJobVacancyPortalException) -> Response:
    return RedirectResponse(url='http://localhost:8000/probation/jobvacancy/index')

@app.exception_handler(RedirectLibraryOccasionPortalException)
def exception_handler_library(request: Request, exc: RedirectLibraryOccasionPortalException) -> Response:
    return RedirectResponse(url='http://localhost:8000/probation/library/index')
  
app.mount("/probation/probationer", probationer_main.probationer_app)
app.mount("/probation/jobvacancy", jobvacancy_main.jobvacancy_app)
app.mount("/probation/library", library_main.library_app)

