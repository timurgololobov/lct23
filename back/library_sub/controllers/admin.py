from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from library_sub.models.data.library import Occasion
from library_sub.models.request.library import OccasionReq, OccasionDetails
from library_sub.services.occasions import OccasionService

router = APIRouter()


# add occasions
@router.post('/occasion/add')
def add_occasions(occasion:OccasionReq):
    occasion = Occasion(classification=occasion.classification, year_published=occasion.year_published, edition=occasion.edition, author=occasion.author, title=occasion.title, occasion_id=occasion.occasion_id)
    occasion_service = OccasionService()
    result = occasion_service.add_occasion(occasion)
    if result == True: 
        return jsonable_encoder(occasion)
    else: 
        return JSONResponse(content={'message': 'occasion insertion not successful'}, status_code=500)

# view occasions
@router.get('/occasion/list')
def view_occasions(): 
    occasion_service = OccasionService()
    return occasion_service.list_occasion()

# delete occasion
@router.delete('/occasion/list')
def delete_occasion(occasion_id:int): 
    occasion_service = OccasionService()
    result = occasion_service.remove_occasion(occasion_id)
    if result == True: 
        return JSONResponse(content={'message': 'occasion insertion successful'}, status_code=201)
    else: 
        return JSONResponse(content={'message': 'occasion insertion not successful'}, status_code=500)

# update occasion info
@router.patch('/occasion/update')
def update_occasion_details(occasion_id:int, occasion_details:OccasionDetails): 
    occasion_dict = occasion_details.dict(exclude_unset=True)
    occasion_service = OccasionService()
    result = occasion_service.update_occasion(occasion_id, occasion_dict )
    if result: 
        return JSONResponse(content={'message':'occasion details updated successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'occasion details update error'}, status_code=500)
