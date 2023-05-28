
from fastapi import FastAPI, Depends
from probationer_sub.controllers import reservations, admin, assignments
from configuration.config import ProbationerSettings, ServerSettings

probationer_app = FastAPI()
probationer_app.include_router(reservations.router)
probationer_app.include_router(admin.router)
probationer_app.include_router(assignments.router)

def build_config(): 
    return ProbationerSettings()

def fetch_config():
    return ServerSettings()

@probationer_app.get('/index')
def index_probationer(config:ProbationerSettings = Depends(build_config), fconfig:ServerSettings = Depends(fetch_config)): 
    return {
        'project_name': config.application,
        'webmaster': config.webmaster,
        'created': config.created,
        'development_server' : fconfig.development_server,
        'dev_port': fconfig.dev_port
        }