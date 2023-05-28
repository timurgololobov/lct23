from fastapi import FastAPI, Depends
from jobvacancy_sub.controllers import admin, assignments, occasions
from configuration.config import JobVacancySettings, ServerSettings

jobvacancy_app = FastAPI()
jobvacancy_app.include_router(admin.router)
jobvacancy_app.include_router(assignments.router)
jobvacancy_app.include_router(occasions.router)

def build_config(): 
    return JobVacancySettings()

def fetch_config():
    return ServerSettings()

@jobvacancy_app.get('/index')
def index_jobvacancy(config:JobVacancySettings = Depends(build_config), fconfig:ServerSettings = Depends(fetch_config)): 
    return {
            'project_name': config.application,
            'webmaster': config.webmaster,
            'created': config.created,
            'production_server' : fconfig.production_server,
            'prod_port' : fconfig.prod_port
            }
