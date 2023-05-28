from typing import Optional
from library_sub.repository.issuance import OccasionIssuanceRepository
from library_sub.models.data.library import OccasionIssuance
from datetime import datetime
class OccasionIssuanceService: 
    
    def __init__(self): 
        self.repo:OccasionIssuanceRepository = OccasionIssuanceRepository()
        
    def add_occasion_release(self, occasion_release:OccasionIssuance): 
        result = self.repo.insert_approval(occasion_release)
        return result
    
    def update_occasion_release(self, approved_id:int, occasion_id:Optional[int] = None, approver:Optional[str] = None): 
        result = False
        if not occasion_id == None: 
            result = self.repo.update_approval_details(approved_id, None, approver )
        elif not approver == None: 
            result = self.repo.update_approval_details(approved_id, approver, None )
        return result 
    
    def remove_occasion_release(self, approved_id:int): 
        result = self.repo.delete_approval(approved_id)
        return result 
    
    def return_issued_occasion(self, issue_id:int, returned_date:datetime): 
        result = self.repo.return_occasion(issue_id, returned_date )
        return result
    
    def list_occasion_release(self): 
        return self.repo.get_all_approvals()