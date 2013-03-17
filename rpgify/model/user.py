from datetime import datetime

from flask.ext.mongokit import Document
import flaskext.bcrypt  as Bcrypt

import utils    as utils
import secrets  as secrets
from rpgify.model import db

class User(Document):
    __collection__='users'
    structure = {
        'email': unicode,
        'passwd': unicode,
        'creation': datetime
    }
    validators = {
        'email': utils.max_length(120)
    }
    required_fields = ['email', 'passwd', 'creation']
    default_values = {'creation': datetime.utcnow}
    use_dot_notation = True
    def __repr__(self):
        return '<User %r>' % (self.email)
    
db.register([User])

def adminAccount(app):
    with app.app_context():
        if not db.User.find_one({'email': secrets.admin['email']}):
            admin = db.User()
            admin.email  = secrets.admin['email']
            admin.passwd = hashPassword(secrets.admin['passwd'])
            admin.save()

def hashPassword(passwd):
    return unicode(Bcrypt.generate_password_hash(passwd))
    
def isCorrectPassword(user, passwd):
    return Bcrypt.check_password_hash(user.passwd, passwd)