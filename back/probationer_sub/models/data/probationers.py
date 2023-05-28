from enum import Enum
from datetime import datetime

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
    

class ProbationerStatus(str, Enum): 
    Freeman='Freeman'
    Sophomore='Стажер'

class Probationer: 
    def __init__(self, stud_id:int, fname:str, lname:str, mname:str, age:int, major:Major, department:str, status:ProbationerStatus ): 
        self.stud_id:int = stud_id
        self.fname:str = fname 
        self.lname:str = lname 
        self.mname:str = mname 
        self.age:int = age 
        self.major:Major = major 
        self.department:str = department 
        self.status:ProbationerStatus = status
        
    def __repr__(self):
        return ' '.join([str(self.stud_id), self.lname, self.mname, self.lname, str(self.age), self.course, self.status])

    def __str__(self): 
        return ' '.join([str(self.stud_id), self.lname, self.mname, self.lname, str(self.age), self.course, self.status]) 
            
class Signup: 
    def __init__(self, sign_id:int, stud_id:int, username:str, password:str):
        self.sign_id:int = sign_id
        self.stud_id:int = stud_id 
        self.username:str = username
        self.password:str = password
        
    def __repr__(self):
        return ' '.join([str(self.sign_id), str(self.stud_id), self.username, self.password])

    def __str__(self): 
        return ' '.join([str(self.sign_id), str(self.stud_id), self.username, self.password])

class Login: 
    def __init__(self, user_id:int, stud_id:int, username:str, password:str): 
        self.user_id:int = user_id 
        self.username:str = username 
        self.password:str = password 
        self.stud_id = stud_id
    
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
    def __init__(self, assgn_id:int, title:str, date_completed:datetime, date_due:datetime, rating:float):
        self.assgn_id:int = assgn_id 
        self.title:str = title 
        self.date_completed:datetime = date_completed 
        self.date_due:datetime = date_due
        self.rating:float = rating 
        
    def __repr__(self): 
        return ' '.join([str(self.assgn_id), self.title, self.date_completed.strftime("%m/%d/%Y, %H:%M:%S"), self.date_due.strftime("%m/%d/%Y, %H:%M:%S"), str(self.rating) ])

    def __expr__(self): 
        return ' '.join([str(self.assgn_id), self.title, self.date_completed.strftime("%m/%d/%Y, %H:%M:%S"), self.date_due.strftime("%m/%d/%Y, %H:%M:%S"), str(self.rating) ])

