from flask import Flask
app = Flask(__name__)
app.config.update(
    # MAIL_SERVER='something',
    # MAIL_USERNAME='username',
    # MAIL_PASSWORD='password',
    # MAIL_PORT=465,
    # MAIL_USE_SSL=True
    
)
app.secret_key = 'Mdkasjdiewud923eqWDEKDOE@DWD#@E12!weomsdc'

import wikisignup.routes