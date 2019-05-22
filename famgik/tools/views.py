from . import tools
from flask import render_template


@tools.route('/')
def index():
    return render_template('tools/index.html')


@tools.route('/test')
def test():
    return render_template('tools/test.html')