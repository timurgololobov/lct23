
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from json import dumps
import httpx
from probationer_sub.models.request.library import OccasionIssuanceReq

router = APIRouter()

@router.get('/access/occasion')
def access_occasion(): 
   with httpx.Client() as client:
    response = client.get("http://localhost:8000/probation/library/occasion/list")
    return response.json()

@router.get('/reserve/occasion')
def reserve_occasion(occasion:OccasionIssuanceReq): 
  with httpx.Client() as client:
     response = client.post("http://localhost:8000/probation/library/occasion/issuance",  data={"occasion":dumps(jsonable_encoder(occasion))})
     return response.content 