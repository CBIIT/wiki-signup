from flask import Flask, render_template, request, redirect
from forms import ContactForm


app = Flask(__name__)      
app.secret_key = 'Mdkasjdiewud923eqWDEKDOE@DWD#@E12!weomsdc'

""" define route for contact form. Because it is 
    the default homepage the route is / """
@app.route('/',methods=['GET', 'POST'])
def contact():
  form = ContactForm()
  if form.validate_on_submit(): # validate form on submit #
    return redirect('/success') # redirect to success page if it passes #
  return render_template('home.html', form=form) # render template again if fails #

if __name__ == '__main__':
  app.run(debug=True)