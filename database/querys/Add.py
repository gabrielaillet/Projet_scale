


from database.querys.Get import *

def save_object_to_db(db_object):
    db.session.add(db_object)
    db.session.commit()


def addStudent(form):
    Student = student(name=form.name.data,surname=form.surname.data)
    save_object_to_db(Student)
    return Student
def addStudentid(form):
    Student = student(student_id=form.student_id.data,name=form.name.data,surname=form.surname.data)
    save_object_to_db(Student)
    return Student
def addTaf(form):
    Taf = taf(name=form.name.data,code=form.code.data)
    save_object_to_db(Taf)
    return Taf


def addTafStudent(form):
    TafStudent = taf_student(student_id=form.student_id.data, taf_id=form.taf_id.data, year=form.year.data)
    save_object_to_db(TafStudent)
    return TafStudent

def addClassProm(form):
    ClassProm = class_prom(student_id = form.student_id.data,year = form.year.data)
    save_object_to_db(ClassProm)
    return ClassProm

