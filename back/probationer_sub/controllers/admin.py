from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from probationer_sub.models.request.probationers import SignupReq, ProbationerReq, ProbationerDetails
from probationer_sub.models.data.probationers import Signup, Login, Probationer
from probationer_sub.services.signup import ProbationerSignupService
from probationer_sub.services.login import ProbationerLoginService
from probationer_sub.services.probationers import ProbationerService

from uuid import uuid4
from json import loads
router = APIRouter()

@router.post('/account/signup')
def signup_probationers(signup:SignupReq): 
    account:Signup = Signup(stud_id=signup.stud_id, username=signup.username, password=signup.password, sign_id=uuid4().int)
    signup_service = ProbationerSignupService()
    result = signup_service.add_signup(account)
    if result == True:
        return jsonable_encoder(account)
    else: 
        return JSONResponse(content={'message':'insertion problem encountered'}, status_code=500)

@router.get('/account/signup/approved')
def approved_signup(sign_id:int): 
    signup_service:ProbationerSignupService = ProbationerSignupService()
    account = signup_service.get_signup(sign_id)
    if not account == None: 
        login = Login(user_id=account.sign_id, stud_id=account.stud_id, username=account.username, password=account.password)
        login_service:ProbationerLoginService = ProbationerLoginService()
        login_service.add_probationer_login(login)
        signup_service.remove_signup(sign_id)
        return jsonable_encoder(account)
    else: 
        return JSONResponse(content={'message':'signup account does not exist'}, status_code=500)
    

@router.post('/login/account')
def login_app(username:str, password:str): 
    login_service:ProbationerLoginService = ProbationerLoginService()
    login = login_service.get_probationer_login(username)
    if login.password == password: 
        return jsonable_encoder(login)
    else: 
        return JSONResponse(content={'message':'login account does not exist'}, status_code=500)

@router.post('/login/password/change')
def change_password(user_id:int, newpass:str):
    login_service:ProbationerLoginService = ProbationerLoginService()
    result = login_service.update_login_password(user_id, newpass)
    if result: 
        return JSONResponse(content={'message':'password changed successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'change password error'}, status_code=500)

@router.post('/profile/add')
def create_profile(profile:ProbationerReq): 
    probationer = Probationer(stud_id=profile.stud_id, fname=profile.fname, lname=profile.lname, \
        mname=profile.mname, age=profile.age, major=profile.major, department=profile.department, status=profile.status)
    probationer_service:ProbationerService = ProbationerService()
    result = probationer_service.add_probationer(probationer)
    if result: 
        return jsonable_encoder(probationer)
    else: 
        return JSONResponse(content={'message':'probationer profile not created'}, status_code=500)

@router.patch('/profile/update')
def update_profile(stud_id:int, profile_details:ProbationerDetails): 
    profile_dict = profile_details.dict(exclude_unset=True)
    probationer_service:ProbationerService = ProbationerService()
    result = probationer_service.update_probationer(stud_id, profile_dict )
    if result: 
        return JSONResponse(content={'message':'profile updated successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'update profile error'}, status_code=500)

@router.get('/profile/list/all')
def list_probationers(): 
    probationer_service:ProbationerService = ProbationerService()
    probationer_list = probationer_service.list_probationers()
    return jsonable_encoder(probationer_list)

