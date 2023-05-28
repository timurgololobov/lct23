from pydantic import BaseModel
from typing import Optional
from jobvacancy_sub.models.data.jobvacancy import Major

class SignupReq(BaseModel):     
    jobvacancy_id:int
    username:str
    password:str

class JobVacancyReq(BaseModel): 
    jobvacancy_id:int
    fname:str
    lname:str
    mname:str
    age:int
    major:Major
    department:str

class JobVacancyDetails(BaseModel): 
    fname:Optional[str] = None
    lname:Optional[str] = None
    mname:Optional[str] = None
    age:Optional[int] = None
    major:Optional[Major] = None
    department:Optional[str] = None

