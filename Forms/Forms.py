from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Regexp, Length, ValidationError
from database.querys.Get import *


class StudentForm(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    name = StringField('prenom de eleve', [ InputRequired(),
        Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
        Length(min=0, max=25, message="Invalid sock name length")
        ])
    surname = StringField('nom de famille de eleve', [ InputRequired(),
        Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
        Length(min=0, max=25, message="Invalid sock name length")
        ])
    # updated - date - handled in the route function
    updated = HiddenField()
    submit = SubmitField('Add/Update Record')


class TafForm(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    name = StringField('nom de la taf', [ InputRequired(),
        Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
        Length(min=0, max=25, message="Invalid sock name length")
        ])
    code = StringField('code de la taf', [ InputRequired(),
        Regexp(r'^[A-Z\s\*\']+$', message="Invalid sock name"),
        Length(min=0, max=7, message="Invalid sock name length")
        ])
    # updated - date - handled in the route function
    updated = HiddenField()
    submit=SubmitField('Add/Update Record')


class TafStudentForm(FlaskForm):

    student_id = IntegerField('id student',validators=[InputRequired()])
    taf_id = StringField('code taf')
    year = StringField('cod')

    def validate_student_id(self,field):
        if(getStudentById(field.data)==None):
            raise ValidationError("violate foreign key rule student id")

    def validate_taf_id(self,field):
        if(getTafById(field.data)==None):
            raise ValidationError("violate foreign key rule taf id")

    updated = HiddenField()
    submit = SubmitField('Add/Update Record')

class classPromForm(FlaskForm):
    student_id = IntegerField('id student', validators=[InputRequired()])
    year = StringField('code')


class EntrepriseForm(FlaskForm):
    entreprise_id = HiddenField()
    year = StringField('code')

class StageForm(FlaskForm):
    stage_id = HiddenField()
    student_id = IntegerField('id student',validators=[InputRequired()])
    entreprise_id = IntegerField('id student',validators=[InputRequired()])
    description = StringField('code')

class ProfileEtudiant(FlaskForm):

    student_id = HiddenField(default=1)
    name = StringField('code')
    surname = StringField('code')
    email = StringField('code')
    etat_civil = StringField('code')
    poste = StringField('code')
    taf = StringField('code')

