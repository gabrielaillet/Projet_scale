import sys

from Forms.Forms import TafStudentForm
from database.querys.Get import *
from database.querys.Delete import *
from database.querys.Add import *
def ChangeProfile(form):
    delStudent(form.student_id.data)
    addStudentid(form)

    tafstudent = taf_student.query.filter_by(student_id = form.student_id.data).all()
    for i in range(len(tafstudent)):
        db.session.delete(tafstudent[i])

    if(form.taf1.data != "pas de taf"):
        TafListSelected = form.taf1.data
        StudentTaf1 = TafStudentForm(student_id = form.student_id.data,taf_id = getIdTafByCode(TafListSelected).taf_id,
                                    year = str(form.year.data))
        addTafStudent(StudentTaf1)

    if (form.taf2.data != "pas de taf"):
        TafListSelected = form.taf2.data
        StudentTaf2 = TafStudentForm(student_id=form.student_id.data, taf_id=getIdTafByCode(TafListSelected).taf_id,
                                     year=str(form.year.data+1))
        addTafStudent(StudentTaf2)

    if (form.taf3.data != "pas de taf"):
        TafListSelected = form.taf3.data
        StudentTaf3 = TafStudentForm(student_id=form.student_id.data, taf_id=getIdTafByCode(TafListSelected).taf_id,
                                     year=str(form.year.data+2))
        addTafStudent(StudentTaf3)

    if (form.taf4.data != "pas de taf"):
        TafListSelected = form.taf4.data
        StudentTaf4 = TafStudentForm(student_id=form.student_id.data, taf_id=getIdTafByCode(TafListSelected).taf_id,
                                     year=str(form.year.data+3))
        addTafStudent(StudentTaf4)

    db.session.commit()


def changeClassProm(form):

    studentInfo = form.student.data.split()
    student_id = student.query.filter_by(name=studentInfo[0],surname=studentInfo[1]).first().student_id
    classProm = getClassProm(student_id)
    db.session.delete(classProm)
    ClassProm = class_prom(student_id = student_id,year = form.year.data)
    save_object_to_db(ClassProm)
    return ClassProm

def changeTaf(form,Taf):
    Taf = taf(name=form.data.name,code=form.data.code,description=form.data.description)
    delTaf(Taf.taf_id)
    save_object_to_db(Taf)
    return Taf