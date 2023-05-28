from typing import Dict , Any
from fastapi.encoders import jsonable_encoder
from library_sub.models.data.librarydb import occasion_tbl
from library_sub.models.data.library import Occasion
from collections import namedtuple

class OccasionRepository: 
    
    def insert_occasion(self, occasion:Occasion) -> bool: 
        try:
            occasion_tbl[occasion.occasion_id] = occasion
        except: 
            return False 
        return True
    
    def update_occasion(self, occasion_id:int, details:Dict[str, Any]) -> bool: 
       try:
           profile = occasion_tbl[occasion_id]
           profile_enc = jsonable_encoder(profile)
           profile_dict = dict(profile_enc)
           profile_dict.update(details)         
           occasion_tbl[occasion_id] = namedtuple("Occasion", profile_dict.keys())(*profile_dict.values())
       except: 
           return False 
       return True
   
    def delete_occasion(self, occasion_id:int) -> bool: 
        try:
            del occasion_tbl[occasion_id] 
        except: 
            return False 
        return True
    
    def get_all_occasions(self):
        return occasion_tbl