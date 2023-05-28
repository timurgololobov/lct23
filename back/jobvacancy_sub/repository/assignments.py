from fastapi.encoders import jsonable_encoder
from typing import Dict , Any
from jobvacancy_sub.models.data.jobvacancydb import jobvacancy_assignments_tbl, probationer_bin_tbl
from jobvacancy_sub.models.data.jobvacancy import Assignment, ProbationerBin
from collections import namedtuple

class AssignmentRepository: 
      
    def insert_assignment(self, assignment:Assignment) -> bool: 
        try:
            jobvacancy_assignments_tbl[assignment.assgn_id] = assignment
        except: 
            return False 
        return True
    
    def update_assignment(self, assgn_id:int, details:Dict[str, Any]) -> bool: 
       try:
           assignment = jobvacancy_assignments_tbl[assgn_id]
           assignment_enc = jsonable_encoder(assignment)
           assignment_dict = dict(assignment_enc)
           assignment_dict.update(details)         
           jobvacancy_assignments_tbl[assgn_id] = namedtuple("Assignment", assignment_dict.keys())(*assignment_dict.values())
       except: 
           return False 
       return True
   
    def delete_assignment(self, assgn_id:int) -> bool: 
        try:
            del jobvacancy_assignments_tbl[assgn_id] 
        except: 
            return False 
        return True
    
    def get_all_assignment(self):
        return jobvacancy_assignments_tbl 
    
class AssignmentSubmissionRepository: 
    
    def create_bin(self, stud_id:int, bin_id:int, jobvacancy_id:int): 
        try:
            probationer_bin = ProbationerBin(bin_id=bin_id, jobvacancy_id=jobvacancy_id, stud_id=stud_id)
            probationer_bin_tbl[bin_id]=probationer_bin
        except: 
            return False 
        return True 
    
    def insert_submission(self, bin_id:int, assignment:Assignment): 
        try:
            probationer_bin:ProbationerBin = probationer_bin_tbl[bin_id]
            probationer_bin.assignment.append(assignment)
        except: 
            return False 
        return True 
    
    def delete_submission(self, bin_id:int, assignment:Assignment ): 
        find_assignment = [work for work in probationer_bin_tbl[bin_id].assignment if work.assgn_id==assignment.assgn_id] 
        if len(find_assignment) == 0: 
            return False 
        else: 
            assignment = find_assignment[0]
            probationer_bin_tbl[bin_id].assignment.remove(assignment)
            return True
        
    def get_submissions(self, bin_id:int): 
        return probationer_bin_tbl[bin_id]
    

