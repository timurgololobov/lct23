from probationer_sub.models.data.probationersdb import stud_signup_tbl
from probationer_sub.models.data.probationers import Signup

class ProbationerSignupRepository: 

    def insert_item(self, item: Signup): 
        try:
            stud_signup_tbl[item.sign_id] = item
        except: 
            return False 
        return True
    
    def delete_item(self, sign_id:int): 
        try: 
            del stud_signup_tbl[sign_id]
        except: 
            return False
        return True 
    
    def get_item(self, sign_id:int): 
        try: 
            account = stud_signup_tbl[sign_id]
        except: 
            return None 
        return account
    
        