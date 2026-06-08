from flask_wtf import FlaskForm
from wtforms.fields import (StringField, PasswordField, IntegerField,
                            DateField, RadioField, SelectField,
                            SubmitField)
from wtforms.validators import DataRequired, equal_to, length
from flask_wtf.file import FileField, FileRequired, FileSize, FileAllowed


class RegisterForm(FlaskForm):
    username = StringField("Enter Username", validators=[
        DataRequired()
    ])
    password = PasswordField("Enter Password", validators=[
        DataRequired(),
        length(min=6, max=24),
    ])
    confirm_password = PasswordField("Confirm Password", validators=[
        DataRequired(),
        equal_to("password", message="პაროლები არ ემთხვევა")
    ])

    register = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField()
    password = PasswordField()

    login = SubmitField("Log In")



class HistoryForm(FlaskForm):
    image = FileField("Upload information poster")
    title = StringField("Enter history Title")
    year = IntegerField("Enter history Year")

    submit = SubmitField("Add information")