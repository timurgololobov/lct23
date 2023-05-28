from probationer_sub.repository.login import ProbationerLoginRepository
from probationer_sub.models.data.probationers import Login

class ProbationerLoginService: 
    
    def __init__(self):
        self.repo:ProbationerLoginRepository = ProbationerLoginRepository()
        
    def add_probationer_login(self, login:Login):
        result = self.repo.insert_login(login)
        return result
    
    def update_login_password(self, user_id:int, newpass:str):
        result = self.repo.update_password(user_id, newpass)
        return result 
    
    def remove_probationer_login(self, user_id:int): 
        result = self.repo.delete_login(user_id)
        return result 
    
    def get_probationer_login(self, username): 
        return self.repo.get_login(username)
        
    def list_login(self): 
        return self.repo.get_all_login()