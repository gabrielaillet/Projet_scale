import sys

from database.querys.Get import *
from database.querys.Delete import *
from database.querys.Add import *
def ChangeProfile(form):
    print(form.student_id.data,file=sys.stderr)
    delStudent(form.student_id.data)
    addStudentid(form)
