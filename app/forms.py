from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import Email, Required, Length
from flask import request

""" define Contact Form and it's fields """
class ContactForm(Form):
	first_name = StringField("First Name", validators=[Required("First Name is required.")])
	last_name = StringField("Last Name", validators=[Required("Last Name is required.")])
	organization = StringField("Organization",validators=[Required("Organization is required.")])
	email = StringField("Email", validators=[Email()])
	phone = StringField("Phone Number",validators=[Required("Phone Number is required.")])
	userName = StringField("NIH User Name")
	areaOfInterest = TextAreaField("Wiki Area of Interest",validators=[Required("Wiki Area of Interest is required.")])
	submit = StringField("Submit")
	clear = StringField("Clear")	
