import sys

from database.querys.Get import *

def save_object_to_db(db_object):
    db.session.add(db_object)
    db.session.commit()


def addStudent(form):
    Student = student(name=form.name.data,surname=form.surname.data)
    save_object_to_db(Student)
    return Student

def addNewStudent(form):
    Student = student(name=form.name.data,surname=form.surname.data)
    save_object_to_db(Student)
    StudentProfile = profile(student_id = Student.student_id,email=form.email.data,
                             post="étudiant",etat_civil=form.etat_civil.data)
    ClassProm = class_prom(student_id=Student.student_id,year=int(form.year.data))
    save_object_to_db(StudentProfile)
    save_object_to_db(ClassProm)
    return Student
def addStudentid(form):
    Student = student(student_id=form.student_id.data,name=form.name.data,surname=form.surname.data)
    save_object_to_db(Student)
    return Student
def addTaf(form):
    Taf = taf(name=form.name.data,code=form.code.data,description='# Linguae habeat deus quaeratur ignes tempora regni\n' +
          '## Et rerum peregrina tamen at longisque mutataque\n' +
          'Lorem markdownum caeloque totidem neque vidit isset repetita aliquisque miseru\n' +
          'solet Erymanthidas cupit relinquit satyros homo qua et edidit. Felicisque regnum' +
          'Hippothousque, futuri pia amore mea: ebur pugnae surrexit posuere frequentes' +
          'primo? Nostra est numina! ' +
          '> Deos tantum haec gratum cui versus quoque Eurystheus palato tenuantur ' +
          '> miserabile et Apollo pinus et artes Cephalus. Et attonitamque comites dextra ' +
          '> dedit, gravis genibus iamque cunctosque a aptius Surrentino meritis posito ' +
          '> iter fero. Et natorum haec **trahit Tusco**, qua lacerat **suis**, nil balatum ' +
          '> divellite cuspis; dum maius, iuvenem relinquunt. Tenebat committitur poteram ' +
          '> de exegit abstulit recens percussa deposuit postquam in est corpora artis mea ' +
          '> gutture dubitat regimen. Nymphis ruptosque illa torum verbenis infectis ' +
          '> positis!' +
          'Sequi iterumque usque, flendoque fieret, moles magis artus **ut** fluit ' +
          '*possent*. Recessu **innumeraeque** artes.' +
          '## Quamvis cum quin virgo trementi populos metalla')
    save_object_to_db(Taf)
    print(Taf.description,file=sys.stderr)
    return Taf


def addTafStudent(form):
    TafStudent = taf_student(student_id=form.student_id.data, taf_id=form.taf_id.data, year=form.year.data)
    save_object_to_db(TafStudent)
    return TafStudent

def addClassProm(form):
    studentInfo = form.student.data.split()
    print(student,file=sys.stderr)
    student_id = student.query.filter_by(name=studentInfo[0],surname=studentInfo[1]).first().student_id
    print(student_id,file=sys.stderr)
    ClassProm = class_prom(student_id = student_id,year = form.year.data)
    save_object_to_db(ClassProm)
    return ClassProm

def addEntreprise(form):
    Entreprise = entreprise(name=form.name.data)
    save_object_to_db(Entreprise)

def checkforSimilarEntreprise(form):
    entreprises = entreprise.query.all()
    for e in entreprises:
        if(e.name.lower().find(form.name.data) > -1):
            return True
    else:
        return False

def returnSimilarEntreprise(form):
    entreprises = entreprise.query.all()
    for e in entreprises:
        if(e.name.lower().find(form.name.data) > -1):
            return e.name
    else:
        Entreprise = entreprise(name=form.name.data)
        save_object_to_db(Entreprise)
        return form.name.data

def addStage(form,idstudent):
    entreprisetext = returnSimilarEntreprise(form)
    idEntreprise = entreprise.query.filter_by(name=entreprisetext).first().entreprise_id
    Stage = stage(student_id=idstudent,description=form.description.data,nom=form.nom.data,info_tuteur=form.info_tuteur.data, entreprise_id=idEntreprise)
    save_object_to_db(Stage)