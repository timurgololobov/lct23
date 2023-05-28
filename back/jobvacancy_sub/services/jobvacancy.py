from typing import List, Dict , Any
from jobvacancy_sub.repository.jobvacancy import JobVacancyRepository
from jobvacancy_sub.models.data.jobvacancy import JobVacancy

class JobVacancyService: 
    
    def __init__(self): 
        self.repo:JobVacancyRepository = JobVacancyRepository()
        
    def add_jobvacancy(self, jobvacancy:JobVacancy): 
        result = self.repo.insert_jobvacancy(jobvacancy)
        return result
    
    def update_jobvacancy(self, jobvacancy_id:int, details:Dict[str, Any]): 
        result = self.repo.update_jobvacancy(jobvacancy_id, details )
        return result 
    
    def remove_jobvacancy(self, jobvacancy_id:int): 
        result = self.repo.delete_jobvacancy(jobvacancy_id)
        return result 
    
    def list_jobvacancy(self): 
        return self.repo.get_all_jobvacancy()
    