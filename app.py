from sqlite3 import Time

import flask
from flask import render_template
from sqlalchemy import create_engine
import sys



import database.database as db
from Forms.Forms import *
from database.querys.Add import *
from database.models import *
from database.database import init_database
from database.querys.Delete import delStudent
from database.querys.change import ChangeProfile


def populate_database():
    db.drop_all()
    db.create_all()
    Student = student(name="Gabriel", surname="Aillet")
    Student2 = student(name="Yves", surname="Bernard")
    Entreprise = entreprise(name="entreprise test")
    Stage = stage(student_id = 1, entreprise_id = 1, description="lorem ipsum")
    Stage2 = stage(student_id=2, entreprise_id=1, description="lorem ipsum2")
    Taf = taf(name="developpement logiciel",code="DCL")
    Taf2 = taf(name="developpement2", code="DCL2")
    studentTaf = taf_student(student_id=1,taf_id=1,year=2022)
    studentTaf2 = taf_student(student_id=2, taf_id=2, year=2024)
    Profile = profile(student_id = 1, email = "test@gmail",etat_civil = "Mr",post = "eleve")
    Prom1 = class_prom(student_id=1, year=2021)
    Prom2 = class_prom(student_id=2, year=2021)
    db.session.add(Prom1)
    db.session.add(Prom2)
    db.session.add(Student)
    db.session.add(Student2)
    db.session.add(Taf)
    db.session.add(Taf2)
    db.session.add(Stage)
    db.session.add(Stage2)
    db.session.add(Entreprise)
    db.session.add(Profile)
    db.session.commit()
    db.session.add(studentTaf)
    db.session.add(studentTaf2)
    db.session.commit()





app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "secret_key1234"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\DELL\\Downloads\\ue_web_example-tp_relations_flask\\database\\database.db"
engine = create_engine("sqlite:///C:\\Users\\DELL\\Downloads\\ue_web_example-tp_relations_flask\\database\\database.db, connect_args={'foreign_keys': True})")

db.init_app(app) # (1) flask prend en compte la base de donnee
with app.test_request_context(): # (2) bloc execute a l'initialisation de Flask
    init_database()
    populate_database()

@app.route("/client/show/<int:id>",methods=["GET", "POST"])
def showClientInfo(id):
    ClassProm = getClassProm(id)
    current_year = datetime.now().year
    Student = getStudentById(id)
    Profil = getProfileByIdStudent(id)
    Taf = getTadOfStudentByStudentId(id)
    """a faire : accordion"""
    return render_template('afficherProfileUtilisateur.html', Student=Student,Profil=Profil,Taf=Taf ,Id=id,
                           classProm=ClassProm, currentYear=current_year)


@app.route("/client/edit/<int:id>",methods=["GET", "POST"])
def changeClientInfo(id):
    """a faire : valeur deja entrée dans l'acordion """
    ClassProm = getClassProm(id)
    current_year = datetime.now().year
    formProfile = ProfileEtudiant(student_id=id)
    if flask.request.method == 'GET':
        Student = getStudentById(id)
        Profile = getProfileByIdStudent(id)
        formProfile = ProfileEtudiant(student_id=id,name=Student.name,surname=Student.surname,email=Profile.email,
                                      etat_civil=Profile.etat_civil,post=Profile.post)
        formProfile.taf1.choices = getTafCode()
        formProfile.taf2.choices = getTafCode()
        formProfile.taf3.choices = getTafCode()
        formProfile.taf4.choices = getTafCode()
        formProfile.year.data = ClassProm.year
        return render_template('ChangePersonnaleData.jinja2',formProfile=formProfile, Id=id,
                               classProm = ClassProm,currentYear=current_year)
    else:

        formProfile.year.data = ClassProm.year
        formProfile.taf1.choices = getTafCode()
        formProfile.taf2.choices = getTafCode()
        formProfile.taf3.choices = getTafCode()
        formProfile.taf4.choices = getTafCode()


        if formProfile.validate_on_submit():
            print(formProfile.taf1.data, file=sys.stderr)
            ChangeProfile(formProfile)
            return flask.redirect("/")
        return render_template('ChangePersonnaleData.jinja2',methods="GET", formProfile=formProfile, Id=id,
                               classProm = ClassProm,currentYear=current_year)
@app.route("/s",methods=["GET", "POST"])
def add_record():
    formStudent = StudentForm()
    formTaf = TafForm()
    formTafStudent = TafStudentForm()


    if formTafStudent.validate_on_submit():
        addTafStudent(formTafStudent)
        return flask.redirect("/")
    if(formStudent.validate_on_submit()):
        addStudent(formStudent)
        return flask.redirect("/")
    if(formTaf.validate_on_submit()):
        addTaf(formTaf)
        return flask.redirect("/")
    return render_template('test.jinja2.html',formTaf=formTaf,formStudent=formStudent ,formTafStudent=formTafStudent)

def tafstudentid(idStudent):
    return  render_template('index.jinja2', )


@app.route("/",methods=["GET", "POST"])
def clean():
    TafofStudent = getAllTafOfStudent()
    Student = student.query.all()
    Taf = taf.query.all()
    TafStudent = taf_student.query.all()
    return render_template('index.jinja2',TafofStudent=TafofStudent, Students=Student,Taf=Taf,TafStudent=TafStudent)

@app.route("/connection",methods=["GET", "POST"])
def connection():
    return render_template('connection.jinja2')


if __name__ == '__main__':
    app.run()
    app.app_context()
