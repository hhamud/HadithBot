from flask import Flask
from os import environ
import hadith 

app = Flask(__name__)
app.run(host= '0.0.0.0', port= environ.get('PORT'))