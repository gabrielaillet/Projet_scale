from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField, IntegerField, BooleanField, SelectMultipleField, RadioField, \
    FieldList, TextAreaField
from wtforms.validators import InputRequired, Regexp, Length, ValidationError
from database.querys.Get import *
from wtforms import SelectField

class StudentForm(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    name = StringField('prenom de eleve', [ InputRequired(),

        Length(min=0, max=25, message="Invalid sock name length")
        ])
    surname = StringField('nom de famille de eleve', [ InputRequired(),

        Length(min=0, max=25, message="Invalid sock name length")
        ])
    # updated - date - handled in the route function
    updated = HiddenField()
    submit = SubmitField('Add/Update Record')


class TafForm(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    taf_name = StringField('nom de la taf', [InputRequired(),
                                             Length(min=0, max=25, message="Invalid sock name length")
                                             ])
    code = StringField('code de la taf', [ InputRequired(),
        Length(min=0, max=7, message="Invalid sock name length")
        ])
    # updated - date - handled in the route function
    updated = HiddenField()
    submit=SubmitField('Add/Update Record')

class TafFormWithDescription(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    taf_name = StringField('nom de la taf', [ InputRequired(),
        Length(min=0, max=25, message="Invalid sock name length")
        ])
    code = StringField('code de la taf', [ InputRequired(),
        Length(min=0, max=7, message="Invalid sock name length")
        ])
    description = TextAreaField('My String',render_kw={'style': 'resize: vertical; width:50%;height:50vh',"rows": 1})
    updated = HiddenField()
    submit=SubmitField('Add/Update Record')

class TafStudentForm(FlaskForm):

    student_id = IntegerField('id student',validators=[InputRequired()])
    taf_id = StringField('code taf')
    year = IntegerField('code')

    def validate_student_id(self,field):
        if(getStudentById(field.data)==None):
            raise ValidationError("violate foreign key rule student id")

    def validate_taf_id(self,field):
        if(getTafById(field.data)==None):
            raise ValidationError("violate foreign key rule taf id")

    updated = HiddenField()
    submit = SubmitField('Add/Update Record')

class classPromForm(FlaskForm):
    current_year = 2015
    year_range = range(current_year, current_year + 30)
    year_choices = [(str(year), str(year)) for year in year_range]
    year = SelectField('Choose a year', choices=year_choices)
    student = SelectField('id student')





class StageForm(FlaskForm):
    name = StringField('nom entreprise')
    description = TextAreaField('Ajoutez une description')
    nom = StringField('codetes')
    info_tuteur = TextAreaField('Ajoutez les coordonnées du tuteur')

class ProfileEtudiantForm(FlaskForm):
    student_id = IntegerField()
    name = StringField('codeyesr')
    surname = StringField('code')
    email = StringField('code')
    etat_civil = RadioField('code',choices=[('Mr', 'Mr'), ('Mme', 'Mme'), ('Autre', 'Autre')])
    post = StringField('code')

    taf1 = RadioField('code',choices=[],default="pas de taf",validators=[InputRequired(message="Please enter taf1")])
    year = IntegerField('Year')

    taf2 = RadioField('code', choices=[],default="pas de taf",validators=[InputRequired(message="Please enter taf2")])


    taf3 = RadioField('code', choices=[],default="pas de taf",validators=[InputRequired(message="Please enter taf3")])


    taf4 = RadioField('code', choices=[],default="pas de taf",validators=[InputRequired(message="Please enter taf4")])

class AddNewStudentForm(FlaskForm):
    Profilename = StringField('code')
    surname = StringField('code')
    email = StringField('code',default="")
    etat_civil = RadioField('code', choices=[('Mr', 'Mr'), ('Mme', 'Mme'), ('Autre', 'Autre')])
    taf1 = RadioField('code',choices=[('Master', 'Master'), ('Fil', 'Fil'), ('Fit', 'Fit'),('Fis','Fis')],default="Fis",validators=[InputRequired(message="Please enter taf1")])
    current_year = 2015
    year_range = range(current_year, current_year + 30)
    year_choices = [(str(year), str(year)) for year in year_range]
    year = SelectField('Choose a year', choices=year_choices)

class EntrepriseForm(FlaskForm):
    entreprise_id = IntegerField()
    name = StringField('code')