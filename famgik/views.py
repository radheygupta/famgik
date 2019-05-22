from flask import current_app as app
from flask import render_template
from flask_login import login_required


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/pretty_print')
@login_required
def pretty_print():
    return "This is a test page."
