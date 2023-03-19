from database.database import db


class student(db.Model):
    student_id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.Text)
    surname = db.Column(db.Text)


class profile(db.Model):
    student_id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column(db.Text)
    etat_civil = db.Column(db.Text)
    post = db.Column(db.Text)


class taf(db.Model):
    taf_id = db.Column('id',db.Integer, primary_key=True)
    name = db.Column(db.Text)
    code = db.Column(db.Text)
    description = db.Column(db.Text)


class taf_student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True, nullable=False)
    taf_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, primary_key=True)


class class_prom(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    year = db.Column(db.Integer)


class entreprise(db.Model):
    entreprise_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)


class stage(db.Model):
    stage_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    entreprise_id = db.Column(db.Integer)
    description = db.Column(db.Text)
    nom = db.Column(db.Text)
