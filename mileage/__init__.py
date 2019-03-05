import os
from flask import Flask
from flask_pymongo import PyMongo
import flask_sijax
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
app.config["MONGO_DBNAME"] = 'mileagedb'
app.config["MONGO_URI"] = "mongodb://localhost:27017/mileagedb"
flask_sijax.Sijax(app)

bcrypt = Bcrypt(app)
mongo = PyMongo(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'warning'


from mileage import routes
