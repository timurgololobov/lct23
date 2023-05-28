from library_sub.models.data.library import OccasionRequest
from library_sub.models.data.librarydb import occasion_request_tbl

class OccasionRequestRepository: 
    
    def insert_request(self, request:OccasionRequest): 
        try: 
            occasion_request_tbl[request.req_id] = request
        except: 
            return False
        return True

    def update_requested_occasion(self, req_id:int, occasion_id:int): 
        try: 
            request = occasion_request_tbl[req_id]
            request.occasion_id = occasion_id
        except: 
            return False
        return True
    
    def delete_request(self, req_id:int): 
        try: 
            del occasion_request_tbl[req_id]
        except: 
            return False
        return True
    
    def get_all_requests(self): 
        return occasion_request_tbl