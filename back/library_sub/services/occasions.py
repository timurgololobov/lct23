from typing import Dict , Any
from library_sub.repository.occasions import OccasionRepository
from library_sub.models.data.library import Occasion

class OccasionService: 
    
    def __init__(self): 
        self.repo:OccasionRepository = OccasionRepository()
        
    def add_occasion(self, occasion:Occasion): 
        result = self.repo.insert_occasion(occasion)
        return result
    
    def update_occasion(self, occasion_id:int, details:Dict[str, Any]): 
        result = self.repo.update_occasion(occasion_id, details )
        return result 
    
    def remove_occasion(self, occasion_id:int): 
        result = self.repo.delete_occasion(occasion_id)
        return result 
    
    def list_occasion(self): 
        return self.repo.get_all_occasions()
    