from datetime import datetime
from typing import Optional
from library_sub.models.data.library import OccasionIssuance
from library_sub.models.data.librarydb import occasion_issuance_tbl

class OccasionIssuanceRepository: 
    
    def insert_approval(self, approved:OccasionIssuance): 
        try: 
            occasion_issuance_tbl[approved.issue_id] = approved
        except: 
            return False
        return True

    def update_approval_details(self, approved_id:int, occasion_id:Optional[int] = None, approver:Optional[str] = None): 
        approved = occasion_issuance_tbl[approved_id]
        try: 
            if not occasion_id == None: 
                approved.occasion_id = occasion_id
            elif not approver == None: 
                approved.approved_by = approver
        except: 
            return False
        return True
    
    def delete_approval(self, approved_id:int): 
        try: 
            del occasion_issuance_tbl[approved_id]
        except: 
            return False
        return True
    
    def return_occasion(self, issue_id:int, returned_date:datetime): 
        try: 
            issuance = occasion_issuance_tbl[issue_id]
            issuance.returned_date = returned_date
            occasion_issuance_tbl[issue_id] = issuance
            
        except: 
            return False
        return True

    def get_all_approvals(self): 
        return occasion_issuance_tbl