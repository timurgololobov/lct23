from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from library_sub.models.data.library import Classification

class OccasionReq(BaseModel): 
        occasion_id:int 
        title:str
        classification:Classification  
        author:str 
        year_published:datetime 
        edition:int  

class OccasionDetails(BaseModel): 
        title:Optional[str] = None
        classification:Optional[Classification] = None  
        author:Optional[str] = None
        year_published:Optional[datetime] = None 
        edition:Optional[int] = None  
        
class OccasionRequestReq(BaseModel): 
        occasion_id:int 
        request_date:datetime  
        status:bool 
    
class OccasionIssuanceReq(BaseModel): 
        req_id:int 
        approved_by:str 
        approved_date:datetime
        
class OccasionReturnReq(BaseModel): 
        issue_id:int 
        returned_date:datetime