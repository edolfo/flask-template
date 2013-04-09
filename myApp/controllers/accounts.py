from flask import Blueprint, render_template, abort, request, session, redirect
from jinja2 import TemplateNotFound
import myApp.model.user as userLib
import simplejson as json

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
    try:
        email = request.form['email']
        passwd = request.form['passwd']
    except:
        return json.dumps(False)
    user = userLib.getUser(email)
    if not user:
        return json.dumps(False)
    if not userLib.isCorrectPassword(user, passwd):
        return json.dumps(False)
    
    session['email'] = email
    #return render_template('index.html')
    return redirect('/')
    
def logout():
    if 'email' in session:
        session.pop('email')
    return render_template('index.html')