import logging
from fastapi import Request

logger = logging.getLogger('uvicorn.access')

def call_api_gateway(request: Request): 
    portal_id = request.path_params['portal_id']
    print(request.path_params)
    if portal_id == str(1): 
        raise RedirectProbationerPortalException() 
    elif portal_id == str(2): 
        raise RedirectJobVacancyPortalException() 
    elif portal_id == str(3): 
        raise RedirectLibraryOccasionPortalException()
    
    
class RedirectProbationerPortalException(Exception):
    pass

class RedirectJobVacancyPortalException(Exception):
    pass

class RedirectLibraryOccasionPortalException(Exception):
    pass
