from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo, URL
from wtforms import ValidationError
from ..models import User

class DocForm(Form):
    title = StringField('Title', validators=[Required()])
    link = StringField('Link to document', validators=[Required(), URL()])
    keywords = StringField('Keywords', validators=[Required()])
    department = SelectField('Department Category', validators=[Required()], choices=[('scc', 'Success'), ('trn', 'Training'), (
        'ops', 'Operations'), ('fnc', 'Finance'), ('rcrt', 'Recruitment'), ('sales', 'Sales'), ('maktng', 'Marketing')])
    submit = SubmitField('submit document')

