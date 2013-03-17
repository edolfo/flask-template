from flask.ext.mongokit import MongoKit
import secrets  as secrets

db = None

def initDB(app):
    app.config['MONGODB_DATABASE']    = secrets.config['MONGODB_DATABASE']
    app.config['MONGODB_HOST']        = secrets.config['MONGODB_HOST']
    app.config['MONGODB_PORT']        = secrets.config['MONGODB_PORT']
    app.config['MONGODB_USERNAME']    = secrets.config['MONGODB_USERNAME']
    app.config['MONGODB_PASSWORD']    = secrets.config['MONGODB_PASSWORD']
    global db 
    db = MongoKit(app)
