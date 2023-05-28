from fastapi import APIRouter

router = APIRouter()

@router.get("/system/{portal_id}")
def access_portal(portal_id:int): 
    return {'message': 'ERP Systems'}

 