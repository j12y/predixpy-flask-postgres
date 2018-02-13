
from flask import Blueprint

# Templates are rendered with Jinja2
ui = Blueprint('ui', __name__, template_folder='templates')

from . import views
