from database.database import db


class studen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    surname = db.Column(db.Text)


class Taf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    code = db.Column(db.Text)

class taf_student(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'),primary_key=True)
    TAF_id = db.Column(db.Integer, db.ForeignKey('id.id'),primary_key=True)
    Année = db.Column('Année',db.Integer,primary_key=True)

                          ,


