from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired,Length, Email
from wtforms.validators import Optional,Regexp

class ContactForm(FlaskForm):
       # Define form fields with validation
       name = StringField("Name", validators=[DataRequired()])
       email = EmailField("Email", validators=[DataRequired(), Email()])
       phone_number = StringField("Phone Number (optional)", validators=[
        Optional(),Regexp(r'^\+?\d{10,15}$', message="Enter a valid phone number with 10 to 15 digits.")
    ])

       submit = SubmitField("Submit")
       
class UsernameForm(FlaskForm):
    username = StringField("Username", validators=[
        DataRequired(),
        Regexp(r'^\w+$', message="Username can only contain letters, numbers, and underscores.")
    ])
    submit = SubmitField("Submit")

class RegistrationForm(FlaskForm):
        username = StringField("Username", validators=[
            DataRequired(),
            Length(min=3, max=15, message="Username must be between 3 and 15 characters.")
        ])
        email = EmailField("Email", validators=[
            DataRequired(),
            Email(message="Please enter a valid email address.")
        ])
        submit = SubmitField("Register")
