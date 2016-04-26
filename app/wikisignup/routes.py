from wikisignup import app
from wikisignup.forms import ContactForm
from flask import render_template, request, redirect

""" define route for contact form. Because it is 
    the default homepage the route is / """
@app.route('/',methods=['GET', 'POST'])
def contact():
  form = ContactForm()
  if form.validate_on_submit(): # validate form on submit #
    return redirect('/success') # redirect to success page if it passes #
  return render_template('home.html', form=form) # render template again if fails #

