from pydantic import BaseModel
from typing import Optional
from probationer_sub.models.data.probationers import ProbationerStatus, Major

class SignupReq(BaseModel):     
    stud_id:int
    username:str
    password:str
    
class ProbationerReq(BaseModel): 
    stud_id:int
    fname:str
    lname:str
    mname:str
    age:int
    major:Major
    department:str 
    status:ProbationerStatus
    
class ProbationerDetails(BaseModel): 
    fname:Optional[str] = None
    lname:Optional[str] = None
    mname:Optional[str] = None
    age:Optional[int] = None
    major:Optional[Major] = None
    department:Optional[str] = None 
    status:Optional[ProbationerStatus] = None