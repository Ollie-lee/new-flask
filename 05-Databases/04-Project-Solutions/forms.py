from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    name = StringField('Name of Tutor:')
    submit = SubmitField('Add Tutor')

class AddCompanyForm(FlaskForm):

    name = StringField('Name of Company:')
    tut_id = IntegerField("Id of Tutor: ")
    submit = SubmitField('Add Company')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Tutor to Remove:')
    submit = SubmitField('Remove Tutor')
