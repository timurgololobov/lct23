from fastapi.encoders import jsonable_encoder
from typing import Dict , Any
from jobvacancy_sub.models.data.jobvacancydb import jobvacancy_tbl
from jobvacancy_sub.models.data.jobvacancy import JobVacancy
from collections import namedtuple

class JobVacancyRepository: 
    
    def insert_jobvacancy(self, jobvacancy:JobVacancy) -> bool: 
        try:
            jobvacancy_tbl[jobvacancy.jobvacancy_id] = jobvacancy
        except: 
            return False 
        return True
    
    def update_jobvacancy(self, jobvacancy_id:int, details:Dict[str, Any]) -> bool: 
       try:
           profile = jobvacancy_tbl[jobvacancy_id]
           profile_enc = jsonable_encoder(profile)
           profile_dict = dict(profile_enc)
           profile_dict.update(details)         
           jobvacancy_tbl[jobvacancy_id] = object_name = namedtuple("JobVacancy", profile_dict.keys())(*profile_dict.values())
       except: 
           return False 
       return True
   
    def delete_jobvacancy(self, user_id:int) -> bool: 
        try:
            del jobvacancy_tbl[user_id] 
        except: 
            return False 
        return True
    
    def get_all_jobvacancy(self):
        return jobvacancy_tbl