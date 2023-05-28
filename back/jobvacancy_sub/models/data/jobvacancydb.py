from typing import Dict
from jobvacancy_sub.models.data.jobvacancy import JobVacancy, Assignment, Login, Signup, ProbationerBin
jobvacancy_tbl:Dict[int, JobVacancy] = dict()
jobvacancy_assignments_tbl:Dict[int, Assignment] = dict()
jobvacancy_login_tbl:Dict[int, Login ] = dict()
jobvacancy_signup_tbl:Dict[int, Signup] = dict()
probationer_bin_tbl:Dict[int, ProbationerBin] = dict()