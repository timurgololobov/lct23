from typing import List, Dict , Any
from jobvacancy_sub.repository.signup import JobVacancySignupRepository
from jobvacancy_sub.models.data.jobvacancy import Signup

class JobVacancySignupService:
    def __init__(self): 
        self.repo:JobVacancySignupRepository = JobVacancySignupRepository()
    
    def add_signup(self, signup: Signup): 
        result = self.repo.insert_item(signup)
        return result
    
    def get_signup(self, sign_id:int): 
        result = self.repo.get_item(sign_id)
        return result
    
    def remove_signup(self, sign_id:int): 
        result = self.repo.delete_item(sign_id)
        return result