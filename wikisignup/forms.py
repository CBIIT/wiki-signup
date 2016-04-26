from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import Email, Required, Length
from flask import request

""" define Contact Form and it's fields """
class ContactForm(Form):
	fields = [
			{'field':'first_name','field_name':'First Name', 'validator':[Required("First Name is required.")]},
			{'field':'last_name','field_name':'Last Name', 'validator':[Required("Last Name is required.")]},
			{'field':'organization','field_name':'Organization', 'validator':[Required("Organization is required.")]},
			{'field':'email','field_name':'Email', 'validator':[Email()]},
			{'field':'phone','field_name':'Phone Number', 'validator':[Required("Phone Number is required.")]},
			{'field':'userName','field_name':'NIH User Name'},
			{'field':'areaOfInterest','field_name':'Wiki Area of Interest', 'validator':[Required("Wiki Area of Interest is required.")]}
			]
	for x in fields:
		print x.has_key('validator')
		if (x.has_key('validator')):
			setattr(Form,x['field'],StringField(x['field_name'], validators=x['validator']))
		else:	
			setattr(Form,x['field'],StringField(x['field_name']))

	submit = StringField("Submit")
	clear = StringField("Clear")	
