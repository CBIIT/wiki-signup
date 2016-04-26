from wikisignup import app
from wikisignup.forms import ContactForm
from flask import render_template, request, redirect
from flask_mail import Mail,Message

""" define route for contact form. Because it is 
    the default homepage the route is / """
@app.route('/',methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	if form.validate_on_submit(): # validate form on submit #
		mail = Mail(app)
		body = ''
		for x in form.fields:
			body+='%s : %s\n' % (x['field_name'],form[x['field']].data)
		msg = Message("NCI Wiki new account request", sender=form.email.data,
	                  recipients=["einolfs@mail.nih.gov"],
	                  body=body)
		mail.send(msg)
		return redirect('/success') # redirect to success page if it passes #
	return render_template('home.html', form=form) # render template again if fails #

""" define success page """
@app.route('/success')
def success():
	return render_template('success.html')