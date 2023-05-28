from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from library_sub.models.data.library import OccasionIssuance, OccasionRequest
from library_sub.models.request.library import OccasionIssuanceReq, OccasionRequestReq, OccasionReturnReq
from library_sub.services.issuance import OccasionIssuanceService
from library_sub.services.reservations import OccasionRequestService

from uuid import uuid4
router = APIRouter()

@router.post('/occasion/request')
def request_occasion(request:OccasionRequestReq): 
    occasion_request = OccasionRequest(status=request.status, request_date=request.occasion_id, occasion_id=request.occasion_id, req_id=uuid4().int) 
    request_service = OccasionRequestService()
    result = request_service.add_occasion_request(occasion_request)
    if result: 
        return jsonable_encoder(occasion_request)
    else: 
        return JSONResponse(content={'message': 'occasion request not successful'}, status_code=500)

@router.post('/occasion/request/list')
def list_requests(): 
    request_service = OccasionRequestService()
    return request_service.list_occasion_request()

@router.post('/occasion/issuance')
def approve_request(approval:OccasionIssuanceReq): 
    occasion_approval = OccasionIssuance(approved_by=approval.approved_by, approved_date=approval.approved_date, req_id=approval.req_id, issue_id=uuid4().int)
    approval_service = OccasionIssuanceService()
    result = approval_service.add_occasion_release(occasion_approval)
    if result: 
        return jsonable_encoder(occasion_approval)
    else: 
        return JSONResponse(content={'message': 'occasion issuance not successful'}, status_code=500)

@router.get('/occasion/issuance/list')
def list_issuances(): 
    approval_service = OccasionIssuanceService()
    return approval_service.list_occasion_release()

@router.post('/occasion/issuance/return')
def return_issued_occasion(returning:OccasionReturnReq): 
    approval_service:OccasionIssuanceService = OccasionIssuanceService()
    result = approval_service.return_issued_occasion(returning.issue_id, returning.returned_date)
    if result: 
        return jsonable_encoder(returning)
    else: 
        return JSONResponse(content={'message': 'occasion issuance not successful'}, status_code=500)