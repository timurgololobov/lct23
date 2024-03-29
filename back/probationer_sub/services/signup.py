from probationer_sub.repository.signup import ProbationerSignupRepository
from probationer_sub.models.data.probationers import Signup  

class ProbationerSignupService: 
    
    def __init__(self): 
        self.repo:ProbationerSignupRepository = ProbationerSignupRepository()
    
    def add_signup(self, signup: Signup): 
        result = self.repo.insert_item(signup)
        return result
    
    def get_signup(self, sign_id:int): 
        result = self.repo.get_item(sign_id)
        return result
    
    def remove_signup(self, sign_id:int): 
        result = self.repo.delete_item(sign_id)
        return result