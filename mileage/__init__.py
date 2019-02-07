import os
from flask import Flask
from flask_pymongo import PyMongo
import flask_sijax

path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
app.config["MONGO_DBNAME"] = 'mileagedb'
app.config["MONGO_URI"] = "mongodb://localhost:27017/mileagedb"

flask_sijax.Sijax(app)

from mileage import routes
