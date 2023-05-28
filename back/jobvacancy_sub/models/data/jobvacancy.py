from typing import List
from enum import Enum
from datetime import datetime

# Здесь была идея сформировать 
class Major(str, Enum): 
    Math='Математика'
    Chem='Химия'
    EEng='Электроснабжение'
    Draver='Водитель'
    Phy='Ученный'
    ChemEng='Инженер'
    Stat='Аналитик'
    CommArts='Дизайнер'
    Archi='Архитектор'
    CS='Специалист по компьютерным наукам'
    IT='Информационные науки'
    Physio='Философ'
    Psych='Психолог'
    Hist='Историк'
    Archeo='Археолог'

class JobVacancy: 
    def __init__(self, jobvacancy_id:int, fname:str, lname:str, mname:str, age:int, major:Major, department:str):
        self.jobvacancy_id:int = jobvacancy_id
        self.fname:str = fname 
        self.lname:str = lname 
        self.mname:str = mname 
        self.age:int = age 
        self.major:Major = major
        self.department:str = department
         
    def __repr__(self): 
        return ' '.join([str(self.jobvacancy_id), self.fname, self.lname, self.mname, str(self.age), self.major, self.department])
    
    def __str__(self): 
        return ' '.join([str(self.jobvacancy_id), self.fname, self.lname, self.mname, str(self.age), self.major, self.department])

class Signup: 
    def __init__(self, sign_id:int, jobvacancy_id:int, username:str, password:str):
        self.sign_id:int = sign_id
        self.jobvacancy_id:int = jobvacancy_id 
        self.username:str = username
        self.password:str = password
        
    def __repr__(self):
        return ' '.join([str(self.sign_id), str(self.stud_id), self.username, self.password])

    def __str__(self): 
        return ' '.join([str(self.sign_id), str(self.stud_id), self.username, self.password])

class Login: 
    def __init__(self, user_id:int, username:str, password:str, jobvacancy_id:int): 
        self.user_id:int = user_id 
        self.username:str = username 
        self.password:str = password 
        self.jobvacancy_id = jobvacancy_id
    
    def __repr__(self): 
        return ' '.join([str(self.user_id), self.username, self.password]) 
    
    def __str__(self):
        return ' '.join([str(self.user_id), self.username, self.password]) 

class Attendance: 
    def __init__(self, attend_id:int, stud_id:int, attend_date:datetime, subject:str, jobvacancy:str): 
        self.attend_id:int = attend_id 
        self.stud_id:int = stud_id
        self.attend_date:datetime = attend_date 
        self.subject:str = subject 
        self.jobvacancy:str = jobvacancy
    def __repr__(self): 
        return ' '.join([str(self.attend_id), str(self.stud_id), self.attend_date.strftime("%m/%d/%Y, %H:%M:%S"), self.subject, self.jobvacancy])

    def __str__(self): 
        return ' '.join([str(self.attend_id), str(self.stud_id), self.attend_date.strftime("%m/%d/%Y, %H:%M:%S"), self.subject, self.jobvacancy])

class Assignment: 
    def __init__(self, assgn_id:int, title:str, date_due:datetime, course:str):
        self.assgn_id:int = assgn_id 
        self.title:str = title 
        self.date_completed:datetime = None
        self.date_due:datetime = date_due
        self.rating:float = 0.0 
        self.course:str = course
        
    def __repr__(self): 
        return ' '.join([str(self.assgn_id), self.title, self.date_completed.strftime("%m/%d/%Y, %H:%M:%S"), self.date_due.strftime("%m/%d/%Y, %H:%M:%S"), str(self.rating) ])

    def __expr__(self): 
        return ' '.join([str(self.assgn_id), self.title, self.date_completed.strftime("%m/%d/%Y, %H:%M:%S"), self.date_due.strftime("%m/%d/%Y, %H:%M:%S"), str(self.rating) ])

class ProbationerBin: 
    def __init__(self, bin_id:int, stud_id:int, jobvacancy_id:int): 
        self.bin_id:int = bin_id 
        self.stud_id:int = stud_id 
        self.jobvacancy_id:int = jobvacancy_id 
        self.assignment:List[Assignment] = list()
        
    
    def __repr__(self): 
        return ' '.join([str(self.bin_id), str(self.stud_id), str(self.jobvacancy_id)])

    def __expr__(self): 
        return ' '.join([str(self.bin_id), str(self.stud_id), str(self.jobvacancy_id)])