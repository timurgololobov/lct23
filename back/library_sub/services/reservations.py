from library_sub.repository.reservations import OccasionRequestRepository
from library_sub.models.data.library import OccasionRequest

class OccasionRequestService: 
    
    def __init__(self): 
        self.repo:OccasionRequestRepository = OccasionRequestRepository()
        
    def add_occasion_request(self, occasion_request:OccasionRequest): 
        result = self.repo.insert_request(occasion_request)
        return result
    
    def update_occasion_request(self, req_id:int, occasion_id:int): 
        result = self.repo.update_requested_occasion(req_id, occasion_id)
        return result 
    
    def remove_occasion_request(self, req_id:int): 
        result = self.repo.delete_request(req_id)
        return result 
    
    def list_occasion_request(self): 
        return self.repo.get_all_requests()
    