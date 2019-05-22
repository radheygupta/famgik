from flask import Blueprint

tools = Blueprint('tools', __name__, url_prefix='/tools', static_folder='static', static_url_path='/static/tools')

from . import views

