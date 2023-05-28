from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from jobvacancy_sub.models.request.jobvacancy import SignupReq, JobVacancyReq, JobVacancyDetails
from jobvacancy_sub.models.data.jobvacancy import Signup, Login, JobVacancy
from jobvacancy_sub.services.signup import JobVacancySignupService
from jobvacancy_sub.services.login import JobVacancyLoginService
from jobvacancy_sub.services.jobvacancy import JobVacancyService

from uuid import uuid4
from json import loads
router = APIRouter()

@router.post('/account/signup')
def signup_jobvacancy(signup:SignupReq): 
    account:Signup = Signup(jobvacancy_id=signup.jobvacancy_id, username=signup.username, password=signup.password, sign_id=uuid4().int)
    signup_service = JobVacancySignupService()
    result = signup_service.add_signup(account)
    if result == True:
        return jsonable_encoder(account)
    else: 
        return JSONResponse(content={'message':'insertion problem encountered'}, status_code=500)

@router.get('/account/signup/approved')
def approved_signup(sign_id:int): 
    signup_service:JobVacancySignupService = JobVacancySignupService()
    account = signup_service.get_signup(sign_id)
    if not account == None: 
        login = Login(user_id=account.sign_id, jobvacancy_id=account.jobvacancy_id, username=account.username, password=account.password)
        login_service:JobVacancyLoginService = JobVacancyLoginService()
        login_service.add_jobvacancy_login(login)
        signup_service.remove_signup(sign_id)
        return jsonable_encoder(account)
    else: 
        return JSONResponse(content={'message':'signup account does not exist'}, status_code=500)
    

@router.post('/login/account')
def login_app(username:str, password:str): 
    login_service:JobVacancyLoginService = JobVacancyLoginService()
    login = login_service.get_jobvacancy_login(username)
    if login.password == password: 
        return jsonable_encoder(login)
    else: 
        return JSONResponse(content={'message':'login account does not exist'}, status_code=500)

@router.post('/login/password/change')
def change_password(user_id:int, newpass:str):
    login_service:JobVacancyLoginService = JobVacancyLoginService()
    result = login_service.update_login_password(user_id, newpass)
    if result: 
        return JSONResponse(content={'message':'password changed successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'change password error'}, status_code=500)

@router.post('/profile/add')
def create_profile(profile:JobVacancyReq): 
    jobvacancy = JobVacancy(jobvacancy_id=profile.jobvacancy_id, fname=profile.fname, lname=profile.lname, \
        mname=profile.mname, age=profile.age, major=profile.major, department=profile.department)
    jobvacancy_service:JobVacancyService = JobVacancyService()
    result = jobvacancy_service.add_jobvacancy(jobvacancy)
    if result: 
        return jsonable_encoder(jobvacancy)
    else: 
        return JSONResponse(content={'message':'probationer profile not created'}, status_code=500)

@router.patch('/profile/update')
def update_profile(jobvacancy_id:int, profile_details:JobVacancyDetails): 
    profile_dict = profile_details.dict(exclude_unset=True)
    jobvacancy_service:JobVacancyService = JobVacancyService()
    result = jobvacancy_service.update_jobvacancy(jobvacancy_id, profile_dict )
    if result: 
        return JSONResponse(content={'message':'profile updated successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'update profile error'}, status_code=500)

@router.get('/profile/list/all')
def list_jobvacancy(): 
    jobvacancy_service:JobVacancyService = JobVacancyService()
    jobvacancy_list = jobvacancy_service.list_jobvacancy()
    return jsonable_encoder(jobvacancy_list)
