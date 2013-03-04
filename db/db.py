from datetime import datetime

from flask import Flask, request, render_template, redirect, url_for
from flask.ext.mongokit import MongoKit, Document

import os

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
    app.config['MONGODB_DATABASE']    = 'SETME'
    app.config['MONGODB_HOST']        = 'SETME'
    app.config['MONGODB_PORT']        = 12345
    app.config['MONGODB_USERNAME']    = 'SETME'
    app.config['MONGODB_PASSWORD']    = 'SETME'
    db = MongoKit(app)
    db.register([Users])
    return app