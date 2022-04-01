import json
import os
from flask_pymongo import PyMongo
from flask import (Flask)
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

f = open("dictionary.json")

dictionary = json.load(f)
for words in dictionary:
    if len(words) < 9:
        if len(words) > 4:
            if "-" not in words:
                print(words)
                sent = {"word": words, "meaning": dictionary[words]}
                print(sent)
                mongo.db.wordlist.insert_one(sent)              


f.close()
