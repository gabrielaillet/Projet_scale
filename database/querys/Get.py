import sys

from database.database import db
from database.models import *


def getStudentById(idStudent):
    Student = student.query.filter_by(id=idStudent).first()
    return Student
def getTafById(idTaf):
    Taf = taf.query.filter_by(id=idTaf).first()
    return Taf

def getTafStudent(idStudent,idTaf,year):
    TafStudent = taf_student.query.filter_by(student_id=idStudent,taf_id=idTaf,year=year).first()
    return TafStudent

def getClassProm(idStudent,year):
    ClassProm = class_prom.query.filter_by(student_id=idStudent,year=year).first()
    return ClassProm
def getClassPromByYear(year):
    ClassProm = class_prom.query.filter_by(year=year)
    return ClassProm
def getEntrepriseById(entreprise_id):
    Entreprise = entreprise.query.filter_by(entreprise_id = entreprise_id).first()
    return Entreprise
def getEntrepriseByName(name):
    Entreprise = entreprise.query.filter_by(name = name).first()
    return Entreprise
def getStageById(stage_id):
    Stage = stage.query.filter_by(stage_id = stage_id).first()
    return Stage
def getStudentByStageByEntrepriseName(name):
    Entreprise = getEntrepriseByName(name)
    Stage = stage.query.filter_by(entreprise_id=Entreprise.entreprise_id).all()
    Stageid = []
    for i in range(len(Stage)):
        Stageid += [Stage[i].student_id]
    print(Stageid, file=sys.stderr)
    Student = student.query.filter(student.student_id.in_(Stageid)).all()
    return Student

def getStudentByTafYear(code_taf,yearStart,yearEnd):
    idtaf = taf.query.filter_by(code=code_taf).first().taf_id
    listStudentTaf = taf_student.query.filter_by(taf_id = idtaf)
    years = [yearStart,yearEnd]

    for i in range(yearEnd - yearStart):
        years += [yearStart + i]

    listStudentTaf = listStudentTaf.filter(taf_student.year.in_(years)).all()
    Studentids = []
    for i in range(len(listStudentTaf)):
        Studentids += [listStudentTaf[i].student_id]
    Student = student.query.filter(student.student_id.in_(Studentids)).all()
    return Student