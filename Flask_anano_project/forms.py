from flask_wtf import FlaskForm
from wtforms.fields import (StringField, PasswordField, IntegerField,
                            DateField, RadioField, SelectField,
                            SubmitField)
from wtforms.validators import DataRequired, equal_to, length
from flask_wtf.file import FileField, FileRequired, FileSize, FileAllowed


class RegisterForm(FlaskForm):
    image = FileField(validators=[
        FileRequired(message="upload the image"),
        FileSize(1024 * 1024 * 3, message="image should be this size"),
        FileAllowed(["png", "jpg", "jpeg"])
    ])
    username = StringField("Enter Username", validators=[
        DataRequired()
    ])
    password = PasswordField("Enter Password", validators=[
        DataRequired(),
        length(min=6, max=24),
    ])
    confirm_password = PasswordField("Confirm Password", validators=[
        DataRequired(),
        equal_to("password", message="not same")
    ])
    mobile = IntegerField(validators=[
        DataRequired()
    ])
    birthdate = DateField()
    gender = RadioField(choices=["Male", "Female", "I'm a megatvin"])
    country = SelectField(choices=["Choose Country", "Georgia", "USA", "Japan"])

    register = SubmitField("Register")



class HistoryForm(FlaskForm):
    image = FileField("Upload information poster")
    title = StringField("Enter history Title")
    year = IntegerField("Enter history Year")

    submit = SubmitField("Add information")