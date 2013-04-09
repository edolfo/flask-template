Flask-template
======

Boilerplate code that adds some structure to a Flask project.  Uses Zurb's Foundation
framework on the frontend and MongoDB for data persistence.  This also includes
session support and login/logout functionality.

* myApp/controllers: Backend server logic
* myApp/model: Database storage abstractions
* myApp/templates: HTML files
* myApp/static: Javascript and CSS files

Installation
============

By default, this is made to work with [cloud9](http://c9.io/) - hence the calls
to the $IP and $PORT environment variables.

Installation requires [flask](http://flask.pocoo.org/), [flask-mongokit](http://pythonhosted.org/Flask-MongoKit/), 
and [flask-bcrypt](http://pythonhosted.org/Flask-Bcrypt/).  In c9, you will need to open a terminal, then run the following:

1. `easy_install pip`
2. `pip install flask`
3. `pip install flask-mongokit`
4. `pip install flask-bcrypt`

Setup
=====

You will need to change the file `db/secrets.template.py` to simply `db/secrets.py`,
and update the values within accordingly.

Then to run the app, in the same folder as `run.py`, run `python run.py`.

Roadmap
=======

* A setup script for customizing the application name
