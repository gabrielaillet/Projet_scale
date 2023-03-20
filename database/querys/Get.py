import sys
from flask import Flask
from database.database import db
from database.models import *
from flask import current_app

def getStudentById(idStudent):
    Student = student.query.filter_by(student_id=idStudent).first()
    return Student

def getStudentNameSurnameForForm():
    Students = student.query.all()
    studentlist = []
    for studen in Students:
        studentlist += [(studen.name  + " " + studen.surname,studen.name  + " " + studen.surname)]
    return studentlist
def getTafById(idTaf):
    Taf = taf.query.filter_by(taf_id=idTaf).first()
    return Taf
def getTadOfStudentByStudentId(idStudent):
    StudentTaf = taf_student.query.filter_by(student_id=idStudent).all()
    Tafids = []
    for i in range(len(StudentTaf)):
        Tafids += [taf.query.filter_by(taf_id = StudentTaf[i].taf_id).first()]


    return Tafids

def getPromotionYear():
    PromYear = set()
    romyear = class_prom.query.all()
    for i in range(len(romyear)):
        PromYear.add(romyear[i].year)
    return list(PromYear)
def getAllTafOfStudent():
    Student = student.query.all()
    TafOfStudent = []
    for i in range(len(Student)):
        TafOfStudent += [[Student[i].student_id,getTadOfStudentByStudentId(Student[i].student_id)]]
    return TafOfStudent
def getTafStudent(idStudent,idTaf,year):
    print(idStudent,idTaf,year,file=sys.stderr)
    TafStudent = taf_student.query.filter_by(student_id=idStudent,taf_id=idTaf,year=year).first()
    return TafStudent

def getClassProm(idStudent):
    ClassProm = class_prom.query.filter_by(student_id=idStudent).first()
    return ClassProm
def getClassPromByYear(year):
    ClassProm = class_prom.query.filter_by(year=year).all()
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

def getProfileByIdStudent(IdStudent):
    print(IdStudent)
    Profile = profile.query.filter_by(student_id = IdStudent).first()
    return Profile

def getTafCode():
    taflist = []
    Taf = taf.query.all()
    for i in range(len(Taf)):
        taflist += [(Taf[i].code,Taf[i].code)]
    return taflist+[("pas de taf","pas de taf")]

def getIdTafByCode(code):
    Taf = taf.query.filter_by(code=code).first()
    return Taf

def isStudentInClassProm(form):
    studentInfo = form.student.data.split()
    student_id = student.query.filter_by(name=studentInfo[0], surname=studentInfo[1]).first().student_id
    classprom = class_prom.query.filter_by(student_id=student_id).first()
    if(classprom == None):
        return False
    return True

def getPromStudents():
    classprm = class_prom.query.all()

    setYear = set()
    for elemt in classprm:
        setYear.add(elemt.year)
    classPromList = []
    listnul = []
    for elemt in setYear:
        classPromList +=  [getClassPromByYear(elemt)]
    for classprm in classPromList:
        l = []
        for e in classprm:
            print(e.student_id)
            l += [e.student_id]
        listnul += [l]
    classPromList = []
    for l in listnul:
        classPromList += [[setYear.pop(),student.query.filter(student.student_id.in_(l)).all()]]
    return classPromList

def getallStageByStudentId(id):
    Stages = stage.query.filter_by(student_id = id).all()
    return Stages