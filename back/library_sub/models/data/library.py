from enum import Enum
from datetime import datetime

class Classification(str, Enum): 
    Non_Fiction='Non-Fiction'
    Fiction='Fiction'
    Science='Science'
    Technology='Technology'
    History='History'
    Arts='Arts'
    Music='Music'
    Travels='Travels'
    Food='Food'
    Engineering='Engineering'

class Occasion: 
    
    def __init__(self, occasion_id:int, title:str, classification:Classification, author:str, year_published:datetime, edition:int): 
        self.occasion_id:int = occasion_id
        self.title = title
        self.classification:Classification = classification 
        self.author:str = author 
        self.year_published:datetime = year_published
        self.edition:int = edition 
    
    def setAllWithKwArgs(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __repr__(self): 
        return ' '.join([str(self.occasion_id), self.classification, self.author, self.year_published.strftime("%m/%d/%Y, %H:%M:%S"), self.edition])
    
    def __str__(self): 
        return ' '.join([str(self.occasion_id), self.classification, self.author, self.year_published.strftime("%m/%d/%Y, %H:%M:%S"), self.edition])

class OccasionRequest: 
    
    def __init__(self, req_id:int, occasion_id:int, request_date:datetime, status:bool): 
        self.req_id:int = req_id
        self.occasion_id:int = occasion_id
        self.request_date:datetime = request_date 
        self.status:bool = status 
    def __repr__(self):
        return ' '.join([str(self.req_id), str(self.occasion_id), self.request_date.strftime("%m/%d/%Y, %H:%M:%S"), str(self.status)])
    
    def __str__(self):
        return ' '.join([str(self.req_id), str(self.occasion_id), self.request_date.strftime("%m/%d/%Y, %H:%M:%S"), str(self.status)])

class OccasionIssuance: 
    def __init__(self, issue_id:int, req_id:int, approved_by:str, approved_date:datetime):
        self.issue_id:int = issue_id 
        self.req_id:int = req_id 
        self.approved_by:str = approved_by
        self.approved_date:datetime = approved_date 
        self.returned_date:datetime = None
    
    def __repr__(self):
        return ' '.join([str(self.issue_id), str(self.req_id), self.approved_by, self.approved_date.strftime("%m/%d/%Y, %H:%M:%S")]) 
    
    def __str__(self):
        return ' '.join([str(self.issue_id), str(self.req_id), self.approved_by, self.approved_date.strftime("%m/%d/%Y, %H:%M:%S")]) 

