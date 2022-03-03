"""
controls the flow through the dev inition website and displays pages and
controls logic
"""
import os
from flask import (
     Flask, flash, render_template,
     redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def homepage():
    """
    displays the homepage
    """
    languages = mongo.db.Languages.find()
    return render_template("homepage.html", languages=languages)


@app.route("/language/<language>")
def language(language):
    """
    displays the content of the language page and controls
    logic of the page
    """
    definitions = mongo.db.devinition.find(language +"_definitions")
    return render_template("/language.html", definitions=definitions)
