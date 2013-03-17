rpgify
======

rpgify your life

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

Then to run the app, in the same folder as `run.py`, run `python run.py`.

Setup
=====

You will need to change the file `db/secrets.template.py` to simply `db/secrets.py`,
and update the values within accordingly.

Notes
=====

This project has modified the basic Flask project by imposing a bit of directory
structure for some more modularity.