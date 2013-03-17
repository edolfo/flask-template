from rpgify import app
import os

port = int(os.environ['PORT'])
host = os.environ['IP']
app.run(port = port, host = host)