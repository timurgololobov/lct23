from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from jobvacancy_sub.models.request.library import OccasionRequestReq, OccasionReturnReq
from json import dumps
import requests

router = APIRouter()

@router.get('/occasions/access/list')
def list_all_occasions(): 
    with requests.Session() as sess:
        response = sess.get('http://localhost:8000/probation/library/occasion/list')
        return response.json()

@router.get('/occasions/request/list')
def list_all_request(): 
    with requests.Session() as sess:
        response = sess.get('http://localhost:8000/probation/library/occasion/request/list',)
        return response.json()

@router.post('/occasions/request/borrow')
def request_borrow_occasion(request:OccasionRequestReq): 
    with requests.Session() as sess:
        response = sess.post('http://localhost:8000/probation/library/occasion/request', data=dumps(jsonable_encoder(request)))
        return response.content

@router.get('/occasions/issuance/list')
def list_all_issuance(): 
    with requests.Session() as sess:
        response = sess.get('http://localhost:8000/probation/library/occasion/issuance/list')
        return response.json()

@router.post('/occasions/returning')
def return_occasion(returning: OccasionReturnReq): 
    with requests.Session() as sess:
        response = sess.post('http://localhost:8000/probation/library/occasion/issuance/return', data=dumps(jsonable_encoder(returning)))
        return response.json()


