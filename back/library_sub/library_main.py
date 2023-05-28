
from fastapi import FastAPI, Depends
from library_sub.controllers import admin, management
from configuration.config import LibraryOccasionSettings

library_app = FastAPI()
library_app.include_router(admin.router)
library_app.include_router(management.router)

def build_config(): 
    return LibraryOccasionSettings()

@library_app.get('/index')
def index_library(config:LibraryOccasionSettings = Depends(build_config) ): 
    return {
            'project_name': config.application,
            'webmaster': config.webmaster,
            'created': config.created
            }