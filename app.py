from sqlite3 import Time

import flask
from flask import render_template, redirect, url_for
from sqlalchemy import create_engine
import sys
from jinja2 import Environment

import database.database as db
from Forms.Forms import *
from database.querys.Add import *
from database.models import *
from database.database import init_database
from database.querys.Delete import delStudent, delEntreprise
from database.querys.change import ChangeProfile, changeClassProm, changeTaf

loremipsum = "# Linguae habeat deus quaeratur ignes tempora regni\n " \
             "## Et rerum peregrina tamen at longisque mutataque\n" \
    "## Et rerum peregrina tamen at longisque mutataque\n" \
    "Lorem markdownum caeloque totidem neque vidit isset repetita" \
             " aliquisque miseru solet Erymanthidas cupit relinquit satyros" \
             " homo qua et edidit. Felicisque regnumHippothousque, futuri " \
             "pia amore mea: ebur pugnae surrexit posuere frequentesprimo? Nostra est numina! \n"




def length_filter(value):
    return len(value)

env = Environment()
env.filters['length'] = length_filter
def populate_database():
    db.drop_all()
    db.create_all()
    Student = student(name="Aillet", surname="Gabriel")
    Student2 = student(name="Bernard", surname="Yves")
    Student3 = student(name="Berger", surname="Arnaud")
    Entreprise = entreprise(name="entreprise test")
    Stage = stage(student_id = 1, entreprise_id = 2, description="lorem ipsum",nom="Data Scientist")
    Stage3 = stage(student_id=1, entreprise_id=1, description="lorem ipsum",nom="Développeur Web")
    Stage2 = stage(student_id=2, entreprise_id=1, description="lorem ipsum2",nom="Cybersécurité")
    Taf = taf(name="developpement logiciel",code="DCL",description=loremipsum)
    Taf2 = taf(name="developpement2", code="DCL2",description=loremipsum)
    Taf3 = taf(name="DEMIN*",code="DEMIN*",description=loremipsum)
    Taf4 = taf(name="DEMIN", code="DEMIN",description=loremipsum)
    studentTaf = taf_student(student_id=1,taf_id=1,year=2022)
    studentTaf2 = taf_student(student_id=2, taf_id=2, year=2024)
    Profile = profile(student_id = 1, email = "test@gmail",etat_civil = "Mr",post = "étudiant")
    Prom1 = class_prom(student_id=1, year=2020)
    Prom2 = class_prom(student_id=2, year=2022)
    db.session.add(Prom1)
    db.session.add(Prom2)
    db.session.add(Student)
    db.session.add(Student2)
    db.session.add(Student3)
    db.session.add(Taf)
    db.session.add(Taf2)
    db.session.add(Taf3)
    db.session.add(Taf4)
    db.session.add(Stage)
    db.session.add(Stage3)
    db.session.add(Stage2)
    db.session.add(Entreprise)
    db.session.add(Profile)
    db.session.commit()
    db.session.add(studentTaf)
    db.session.add(studentTaf2)
    db.session.commit()





app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "secret_key1234"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\Yves\\Desktop\\WEB\\Projet_scale-master\\database\\database.db"
db.init_app(app) # (1) flask prend en compte la base de donnee
with app.test_request_context(): # (2) bloc execute a l'initialisation de Flask
    init_database()
    populate_database()



@app.route("/<string:name>/prom",methods=["GET", "POST"])
def prom(name):
    classProm = getPromStudents()
    print(classProm,file=sys.stderr)
    return render_template("PromotionTab.html",classProm=classProm,name=name,id=1)

@app.route("/<string:name>/del/entreprise/<int:id>",methods=["GET", "POST"])
def supprimerEntreprise(name,id):
    delEntreprise(id)
    return  redirect(url_for('EntrepriseTab',name=name))

@app.route("/<string:name>/entreprise",methods=["GET", "POST"])
def EntrepriseTab(name):
    Entreprise = entreprise.query.all()
    print(Entreprise)
    return render_template("entrepriseTab.html",Entreprise=Entreprise,name=name,id=1)
@app.route("/<string:name>/show/<int:id>/",methods=["GET", "POST"])
def showClientInfo(name,id):
    CanModify = str(id) == name
    ClassProm = getClassProm(id)
    if(ClassProm == None):
        ClassProm = dict()
        ClassProm['year'] = 0
    current_year = datetime.now().year
    print(ClassProm.year)
    Student = getStudentById(id)
    Profil = getProfileByIdStudent(id)
    Taf = getTadOfStudentByStudentId(id)
    Stages = getallStageByStudentId(id)
    lenStage=length_filter(Stages)
    Entreprises=[]
    for stage in Stages:
        entreprise_obj = entreprise.query.filter_by(entreprise_id=stage.entreprise_id).first()
        if entreprise_obj:
            Entreprises.append(entreprise_obj.name)
    print(Entreprises)
    print(Stages)
    return render_template('afficherProfileUtilisateur.html', Student=Student,Profil=Profil,Taf=Taf ,id=id,
                           classProm=ClassProm, currentYear=current_year,canModify=CanModify,name=name, Stages=Stages
                           ,Entreprises=Entreprises,lenStage=lenStage)
@app.route("/<string:name>/show/<string:TafCode>",methods=["GET", "POST"])
def ShowTaf(name,TafCode):
    Taf = getIdTafByCode(TafCode)
    if(Taf != None):
        return render_template('TafDescription.html',Taf=Taf,name=name)

@app.route("/<string:name>/edit/<string:TafCode>",methods=["GET", "POST"])
def editTaf(name,TafCode):
    if(name == "Admin"):
        Taf = getIdTafByCode(TafCode)
        if(Taf != None):
            if flask.request.method == 'GET':
                TafForm = TafFormWithDescription(name=Taf.name,code=Taf.code,description=Taf.description)
                return render_template('TafEdit.html',name=name, Taf=Taf, TafForm=TafForm)
            if flask.request.method == 'POST':
                TafForm = TafFormWithDescription()

                if(TafForm.validate_on_submit()):
                    print(TafForm.description, file=sys.stderr)
                    changeTaf(TafForm,Taf)
                    return redirect(url_for("ShowTaf",name=name,TafCode=TafForm.code.data))
                return render_template('TafEdit.html',name=name, Taf=Taf, TafForm=TafForm)
@app.route("/<string:name>/edit/",methods=["GET", "POST"])
def adminTab(name):
    if (name == "Admin"):
        NewStudentForm = AddNewStudentForm()
        formTaf = TafForm()
        formTafStudent = TafStudentForm()
        formClassProm = classPromForm()
        entrepriseForm = EntrepriseForm()
        formClassProm.student.choices = getStudentNameSurnameForForm()
        Tafs = taf.query.all()
        Student = student.query.all()
        Promotion = getPromotionYear()
        if flask.request.method == 'GET':

                return render_template('AdminTab.html', NewStudentForm=NewStudentForm, formTaf=formTaf,
                                       formTafStudent=formTafStudent, Tafs=Tafs, Student=Student,
                                       Promotion=Promotion,name=name,formClassProm=formClassProm,
                                       entrepriseForm=entrepriseForm)
        if flask.request.method == 'POST':

                formTaf.validate()
                if(formTaf.validate_on_submit()):
                    addTaf(formTaf)
                    Tafs = taf.query.all()

                if(formTafStudent.validate_on_submit()):
                    addTafStudent(formTafStudent)
                    return redirect(url_for('tableaux',name=name))
                if(NewStudentForm.validate_on_submit()):
                    addNewStudent(NewStudentForm)
                if(entrepriseForm.validate_on_submit()):
                    if(not checkforSimilarEntreprise(entrepriseForm)):
                        addEntreprise(entrepriseForm)
                        redirect(url_for('EntrepriseTab',name=name))


                if(formClassProm.validate_on_submit()):

                    if(isStudentInClassProm(formClassProm)):
                        changeClassProm(formClassProm)

                    else:
                        addClassProm(formClassProm)

                return render_template('AdminTab.html', NewStudentForm=NewStudentForm, formTaf=formTaf,
                                       formTafStudent=formTafStudent, Tafs=Tafs, Student=Student,
                                       Promotion=Promotion, name=name, formClassProm=formClassProm,
                                       entrepriseForm=entrepriseForm)
@app.route("/<string:name>/edit/<int:id>",methods=["GET", "POST"])
def changeClientInfo(name,id):
    ClassProm = getClassProm(id)
    current_year = datetime.now().year
    formProfile = ProfileEtudiantForm(student_id=id)
    Student = getStudentById(id)
    Profile = getProfileByIdStudent(id)
    Taf = getTadOfStudentByStudentId(id)
    stageform = StageForm()
    if flask.request.method == 'GET':
        formProfile = ProfileEtudiantForm(student_id=id, name=Student.name, surname=Student.surname, email=Profile.email,
                                          etat_civil=Profile.etat_civil, post=Profile.post, Student=Student)
        tafCode = getTafCode()
        if(len(Taf) >= 1):

            formProfile.taf1.data  = Taf[0].code
        if (len(Taf)>= 2):
            formProfile.taf2.data  = Taf[1].code

        if (len(Taf)>= 3):
            formProfile.taf3.data = Taf[2].code

        if(len(Taf) >= 4):
            formProfile.taf4.data = Taf[3].code

        formProfile.taf1.choices = tafCode
        formProfile.taf2.choices = tafCode
        formProfile.taf3.choices = tafCode
        formProfile.taf4.choices = tafCode
        formProfile.year.data = ClassProm.year
        return render_template('ChangePersonnaleData.jinja2',formProfile=formProfile, id=id,
                               classProm = ClassProm,currentYear=current_year,name=name,Student=Student,stageform=stageform)
    else:

        formProfile.year.data = ClassProm.year
        formProfile.taf1.choices = getTafCode()
        formProfile.taf2.choices = getTafCode()
        formProfile.taf3.choices = getTafCode()
        formProfile.taf4.choices = getTafCode()

        if stageform.validate_on_submit():
            addStage(stageform,id)

        if formProfile.validate_on_submit():
            print(formProfile.taf1.data, file=sys.stderr)
            ChangeProfile(formProfile)
            return redirect(url_for('showClientInfo', name=name,id=id))

        return render_template('ChangePersonnaleData.jinja2',methods="GET", formProfile=formProfile, id=id,
                               classProm = ClassProm,currentYear=current_year,name=name,Namecompte=name,Student=Student,stageform=stageform)
@app.route("/s/3",methods=["GET", "POST"])
def add_record():
    formStudent = StudentForm()
    formTaf = TafForm()
    formTafStudent = TafStudentForm()

    if formTafStudent.validate_on_submit():
        addTafStudent(formTafStudent)
        return render_template('test.jinja2.html', formTaf=formTaf, formStudent=formStudent,
                               formTafStudent=formTafStudent)

    if(formStudent.validate_on_submit()):
        addStudent(formStudent)
        return render_template('test.jinja2.html', formTaf=formTaf, formStudent=formStudent,
                               formTafStudent=formTafStudent)

    if(formTaf.validate_on_submit()):
        addTaf(formTaf)
        return render_template('test.jinja2.html', formTaf=formTaf, formStudent=formStudent,
                               formTafStudent=formTafStudent)

    return render_template('test.jinja2.html',formTaf=formTaf,formStudent=formStudent ,formTafStudent=formTafStudent)




@app.route("/<string:name>",methods=["GET", "POST"])
def tableaux(name):
    TafofStudent = getAllTafOfStudent()
    Student = student.query.all()
    Taf = taf.query.all()
    TafsTrio =[]
    lastTrio = []
    entiertrio = len(Taf)%3
    for i in range(0,int((len(Taf)-entiertrio)/3),3):
        TafsTrio += [[Taf[i],Taf[i+1],Taf[i+2]]]
    for j in range((len(Taf)-entiertrio),len(Taf)):
        lastTrio += [Taf[j]]
    TafsTrio += [lastTrio]
    TafStudent = taf_student.query.all()

    NbreStudent = len(student.query.all())
    NbreEntreprise = len(entreprise.query.all())

    if(name == "Admin"):
        return render_template('index.jinja2', TafofStudent=TafofStudent, Students=Student, Taf=Taf,
                               TafStudent=TafStudent,
                               name=name, id=0, NbreStudent=NbreStudent,
                               NbreEntreprise=NbreEntreprise,TafsTrio=TafsTrio)


    return render_template('index.jinja2',TafofStudent=TafofStudent, Students=Student,Taf=Taf,TafStudent=TafStudent,
                           name=name,id=1,NbreStudent=NbreStudent,
                           NbreEntreprise=NbreEntreprise,TafsTrio=TafsTrio)

@app.route("/",methods=["GET", "POST"])
def connection():
    return render_template('connection.jinja2')


if __name__ == '__main__':
    app.run()
    app.app_context()
