from flask import Flask, render_template, request, redirect
from forms import ContactForm


app = Flask(__name__)      
app.secret_key = 'Mdkasjdiewud923eqWDEKDOE@DWD#@E12!weomsdc'

@app.route('/',methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if form.validate_on_submit():
    return redirect('/success')
  return render_template('home.html', form=form)

 
if __name__ == '__main__':
  app.run(debug=True)