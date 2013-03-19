from flask import Flask, render_template
import os, sys
from myApp.model import initDB, db

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='%%',
        variable_end_string='%%',
        comment_start_string='<#',
        comment_end_string='#>',
    ))

app = CustomFlask('myApp')
initDB(app)

from controllers import root, accounts
import model.user  as userLib
from routes import createRoutes

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

createRoutes()
app.register_blueprint(root.views)
app.register_blueprint(accounts.views)

app.static_folder = 'static'
app.template_folder = 'templates'
app.debug = True

userLib.adminAccount(app)
