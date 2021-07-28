from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import Email



class LoginForm(FlaskForm):
    email = StringField("Email", validators=[Email()])
    password = PasswordField("Password")
    
