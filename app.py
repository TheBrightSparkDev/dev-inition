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
    
    return render_template("homepage.html")


# sign up section
@app.route("/signup", methods=["GET", "POST"])
def register():
    """
    displays signup page and controls logic on the page
    """

    if request.method == "POST":
        # check if usernmae in form element already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the newly created user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("registration successful")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# sign in section
@app.route("/signin", methods=["GET", "POST"])
def login():
    """
    displays sign in and controls logic on sign in page
    """

    if request.method == "POST":
        # check if usernmae in form element exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matched the db
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("username and/or password is incorrect")
                return redirect(url_for("signin"))
        else:
            # username doesnt exist
            flash("username and/or password is incorrect")
            return redirect(url_for("signin"))
    return render_template("signin.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
