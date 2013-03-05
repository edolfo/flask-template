from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
import rpgify.db.user as userLib

views = Blueprint('accounts', __name__, template_folder='templates')

@views.route('/signup')
def signup():
    try:
        return render_template('signup.html')
    except TemplateNotFound:
        abort(404)
    
@views.route('/login')
def login():
    try:
        return render_template('login.html')
    except TemplateNotFound:
        abort(404)
        
@views.route('/login/handler')
def login_handler():
    email = request['email']
    passwd = request['passwd']