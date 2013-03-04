from flask import Flask, render_template
import os, sys
from controllers import root
import db.db as dbLib

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

app = CustomFlask('rpgify')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

app.register_blueprint(root.views)

if __name__ == "__main__":
    app.static_folder = 'static'
    app.template_folder = 'templates'
    port = int(os.environ['PORT'])
    host = os.environ['IP']
    app.debug = True
    
    #DB connection
    app = dbLib.initDB(app)
    
    app.run(port = port, host = host)