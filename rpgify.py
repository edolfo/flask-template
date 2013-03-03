from flask import Flask
import os, sys
from controllers import root

app = Flask('rpgify')
app.register_blueprint(root.views)

if __name__ == "__main__":
    app.static_folder = 'static'
    app.template_folder = 'templates'
    port = int(os.environ['PORT'])
    host = os.environ['IP']
    app.debug = True
    app.run(port = port, host = host)