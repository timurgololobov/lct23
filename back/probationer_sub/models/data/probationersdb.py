from typing import Dict
from probationer_sub.models.data.probationers import Login, Probationer, Signup, Assignment

probationers_tbl:Dict[int, Probationer] = dict()
stud_login_tbl:Dict[int, Login ] = dict()
stud_signup_tbl:Dict[int, Signup] = dict()

