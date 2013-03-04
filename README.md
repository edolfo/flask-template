rpgify
======

rpgify your life

Installation
============

By default, this is made to work with [cloud9](http://c9.io/) - hence the calls
to the $IP and $PORT environment variables.

Installation requires [flask](http://flask.pocoo.org/).  In c9, you will need to
open a terminal, then run the following:

# `easy_install pip`
# `pip install flask`

Then to run the app, in the same folder as `rpgify.py`, run `python rpgify.py`.

Setup
=====

You will need to change the file `db/secrets.template.py` to simply `secrets.py`,
and update the values within accordingly.