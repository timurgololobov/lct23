from typing import List, Dict , Any

from fastapi.encoders import jsonable_encoder
from probationer_sub.models.data.probationers import Probationer
from probationer_sub.models.data.probationersdb import probationers_tbl
from collections import namedtuple

class ProbationerRepository: 
    
    def insert_probationer(self, probationer:Probationer) -> bool: 
        try:
            probationers_tbl[probationer.stud_id] = probationer
        except: 
            return False 
        return True
    
    def update_probationer(self, stud_id:int, details:Dict[str, Any]) -> bool: 
       try:
           profile = probationers_tbl[stud_id]
           profile_enc = jsonable_encoder(profile)
           profile_dict = dict(profile_enc)
           profile_dict.update(details)         
           probationers_tbl[stud_id] = namedtuple("Probationer", profile_dict.keys())(*profile_dict.values())
       except: 
           return False 
       return True
   
    def delete_probationer(self, user_id:int) -> bool: 
        try:
            del probationers_tbl[user_id] 
        except: 
            return False 
        return True
    
    def get_all_probationers(self):
        return probationers_tbl