from wtforms import Form
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField
from flask_wtf import FlaskForm

from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField
from wtforms import validators

def mi_Validacion(form, field):
    if len(field.data) == 0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula = StringField('Matricula',[
                            validators.DataRequired(message='El campo es requerido'),
                            validators.length(min=4, max=10, message='long de campo 4 min and 5 max')])
    nombre = StringField('Nombre',[
                         validators.DataRequired(message='El campo es requerido')])
    apaterno = StringField('Apaterno', [mi_Validacion])
    amaterno = StringField('Amaterno')
    email = EmailField('Email')

class LoginForm(Form):
    username = StringField('usuario', [
                            validators.DataRequired(message='El campo es requerido'),
                            validators.length(min=4, max=10, message='El largo del texto tiene que estar entre 4 y 10')])
    
    password = StringField('contraseña',[
                            validators.DataRequired(message='El campo es requerido'),
                            validators.length(min=4, max=10, message='long de campo 4 min and 5 max')])

class Languages(Form):
    spanish = StringField('Español', [
                            validators.DataRequired(message='El campo es requerido'),
                            validators.length(min=2, max=10, message='El largo del texto tiene que estar entre 2 y 10')])
    english = StringField('Inglés', [
                            validators.DataRequired(message='El campo es requerido'),
                            validators.length(min=1, max=10, message='El largo del texto tiene que estar entre 1 y 10')])