from flask import Flask
import os, sys

app = Flask('rpgify')

@app.route("/")
def hello():
    return "Hello world!"
    
if __name__ == "__main__":
    app.static_folder = 'static'
    app.template_folder = 'templates'
    port = int(os.environ['PORT'])
    host = os.environ['IP']
    app.debug = True
    app.run(port = port, host = host)