import flask
from os import environ

app = flask(__name__)
app.run(host= '0.0.0.0', port= environ.get('PORT'))