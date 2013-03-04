from datetime import datetime

from flask import Flask, request, render_template, redirect, url_for
from flask.ext.mongokit import MongoKit, Document

import secrets as secrets

class Users(Document):
    __collection__ = 'users'
    structure = {
        'email': unicode,
        'pass': unicode,
        'creation': datetime,
    }
    required_fields = ['email', 'pass', 'creation']
    default_values = {'creation': datetime.utcnow}
    use_dot_notation = True

def initDB(app):
    app.config['MONGODB_DATABASE']    = secrets.config['MONGODB_DATABASE']
    app.config['MONGODB_HOST']        = secrets.config['MONGODB_HOST']
    app.config['MONGODB_PORT']        = secrets.config['MONGODB_PORT']
    app.config['MONGODB_USERNAME']    = secrets.config['MONGODB_USERNAME']
    app.config['MONGODB_PASSWORD']    = secrets.config['MONGODB_PASSWORD']
    db = MongoKit(app)
    db.register([Users])
    return app