from typing import Dict , Any
from probationer_sub.repository.probationers import ProbationerRepository
from probationer_sub.models.data.probationers import Probationer

class ProbationerService: 
    
    def __init__(self): 
        self.repo:ProbationerRepository = ProbationerRepository()
        
    def add_probationer(self, probationer:Probationer): 
        result = self.repo.insert_probationer(probationer)
        return result
    
    def update_probationer(self, stud_id:int, details:Dict[str, Any]): 
        result = self.repo.update_probationer(stud_id, details)
        return result 
    
    def remove_probationer(self, stud_id:int): 
        result = self.repo.delete_probationer(stud_id)
        return result 
    
    def list_probationers(self): 
        return self.repo.get_all_probationers()
    
    