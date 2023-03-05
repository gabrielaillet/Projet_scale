import sys

from database.database import db
from database.querys.Get import *
def delStudent(id):
    Student = getStudentById(id)
    db.session.delete(Student)
    db.session.commit()
def delTaf(id):
    Taf = getTafById(id)
    db.session.delete(Taf)
    db.session.commit()

def delTafStudent(idStudent,idTaf,Year):
    TafStudent = getTafStudentById(idStudent,idTaf,Year)
    db.session.delete(TafStudent)
    db.session.commit()

def delClassProm(idStudent,year):
    ClassProm = getClassProm(idStudent,year)
    db.session.delete(ClassProm)
    db.session.commit()

def delEntreprise(idEntreprise):
    Entreprise = getEntreprise(idEntreprise)
    db.session.delete((Entreprise))
    db.session.commit()

def delStage(idStage):
    Stage = getStageById(idStage)
    db.session.delete(Stage)
    db.session.commit()