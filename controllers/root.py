from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

views = Blueprint('root', __name__, template_folder='templates')

@views.route('/')
def index():
    try:
        return render_template('base.html')
    except TemplateNotFound:
        abort(404)