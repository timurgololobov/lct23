from jobvacancy_sub.repository.login import JobVacancyLoginRepository
from jobvacancy_sub.models.data.jobvacancy import Login


class JobVacancyLoginService: 
    
    def __init__(self):
        self.repo:JobVacancyLoginRepository = JobVacancyLoginRepository()
        
    def add_jobvacancy_login(self, login:Login):
        result = self.repo.insert_login(login)
        return result
    
    def update_login_password(self, user_id:int, newpass:str):
        result = self.repo.update_password(user_id, newpass)
        return result 
    
    def remove_jobvacancy_login(self, user_id:int): 
        result = self.repo.delete_login(user_id)
        return result 
    
    def get_jobvacancy_login(self, username): 
        return self.repo.get_login(username)
        
    def list_login(self): 
        return self.repo.get_all_login()