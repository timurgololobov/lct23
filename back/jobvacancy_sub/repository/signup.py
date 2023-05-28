from jobvacancy_sub.models.data.jobvacancydb import jobvacancy_signup_tbl
from jobvacancy_sub.models.data.jobvacancy import Signup

class JobVacancySignupRepository: 

    def add_item(self, item: Signup): 
        try:
            jobvacancy_signup_tbl[item.sign_id] = item
        except: 
            return False 
        return True
    
    def remove_item(self, sign_id:int): 
        try: 
            del jobvacancy_signup_tbl[sign_id]
        except: 
            return False
        return True 

    def get_item(self, sign_id:int): 
        try: 
            account = jobvacancy_signup_tbl[sign_id]
        except: 
            return None 
        return account
    