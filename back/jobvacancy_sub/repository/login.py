from typing import List 
from jobvacancy_sub.models.data.jobvacancydb import jobvacancy_signup_tbl, jobvacancy_login_tbl
from jobvacancy_sub.models.data.jobvacancy import Login

class JobVacancyLoginRepository: 
    
    def insert_login(self, sign_id:int) -> bool: 
        try:
            account = jobvacancy_signup_tbl[sign_id]
            login = Login(user_id=account.sign_id, jobvacancy_id=account.jobvacancy_id, username=account.username, password = account.password)
            jobvacancy_signup_tbl[account.jobvacancy_id] = login 
        except: 
            return False 
        return True
    
    def update_password_userid(self, user_id:int, newpass:str) -> bool:
        try:
            login = jobvacancy_login_tbl[user_id]
            login.password = newpass
        except:
            return False 
        return True
    
    def delete_login(self, user_id:int) -> bool: 
        try:
           del jobvacancy_login_tbl[user_id]
        except:
            return False 
        return True
    
    def get_all_login(self) -> List[Login]: 
        return jobvacancy_login_tbl.values();