from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
import rpgify.model.user as userLib

views = Blueprint('accounts', __name__, template_folder='templates')

def signup():
    try:
        return render_template('signup.html')
    except TemplateNotFound:
        abort(404)
    
def login():
    try:
        return render_template('login.html')
    except TemplateNotFound:
        abort(404)

def login_handler():
    email = request['email']
    passwd = request['passwd']