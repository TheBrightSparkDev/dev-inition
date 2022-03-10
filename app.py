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
from datetime import datetime

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
def signup():
    """
    displays signup page and controls logic on the page
    """

    if request.method == "POST":
        # check if usernmae in form element already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signin"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "friends": []
        }
        mongo.db.users.insert_one(register)

        # put the newly created user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("registration successful")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("signup.html")


# sign in section
@app.route("/signin", methods=["GET", "POST"])
def signin():
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
            return redirect(url_for("signup"))
    return render_template("signin.html")


@app.route("/signout")
def signout():
    """
    logs the user out
    """
    flash("you have been logged out")
    session.pop("user")
    return redirect(url_for("homepage"))


# profile section
@app.route("/profile/<username>")
def profile(username):
    """
    displays profile and controls logic on profile page
    """
    if username == "guest":
        session['user'] = "guest"
    else:
        session['user'] = username
    return render_template("profile.html", username=username)


@app.route("/friend_picker/<username>")
def friend_picker(username):
    """
    displays friend picker page and controls logic for page
    """
    user = mongo.db.users.find_one({"username": username.lower()})
    friends = user["friends"]

    return render_template('friend_picker.html', friends=friends)



@app.route("/add_friend", methods=["GET", "POST"])
def add_friend():
    """
    displays friend picker page and controls logic for page
    """
    add_user= request.form.get("username")
    user = mongo.db.users.find_one( {"username": session['user'].lower() })
    friends = user["friends"]
    if request.method == "POST":
        if request.form.get("username") not in friends:
            mongo.db.users.update_many(
                {'username': session['user']}, {'$push': {"friends": add_user}})
            flash("Friend added")
        else:
            flash("You are already friends")
    return render_template('add_friend.html', friends=friends)


@app.route("/create_challenge/<friend>", methods=["GET", "POST"])
def create_challenge(friend):
    """
    displays create challenge page and controls logic
    also sends a challenge to the database
    """
    if request.method == "POST":
        now = datetime.now()
        format_now = now.strftime("%d/%m/%Y %H:%M:%S")
        word = request.form.get("word").lower()
        letter = request.form.get("letters").lower()
        challenge = {"for": friend,
                     "word": word,
                     "letters": letter,
                     "from": session['user'],
                     "state": "created",
                     "created_date": format_now,
                     "updated_date": format_now,
                     "guess_1":"",
                     "guess_2":"",
                     "guess_3":"",
                     "guess_4":"",
                     "guess_5":"",
                     "guess_6":"",
                     }
        mongo.db.challenges.insert_one(challenge)
        flash("challenge sent")
    return render_template('create_challenge.html', friend=friend)


@app.route("/challenges")
def challenges():
    """
    displays the challenges for an individual
    """
    user = session['user']
    challenges = list(mongo.db.challenges.find({"for": user}))
    return render_template('challenges.html', challenges=challenges)


@app.route("/sent_challenges")
def sent_challenges():
    """
    displays the challenges sent by an individual
    """
    user = session['user']
    challenges = list(mongo.db.challenges.find({"from": user}))
    return render_template('sent_challenges.html', challenges=challenges)


@app.route("/game/<challenge>", methods=["GET", "POST"])
def game(challenge):
    """
    displays the main game and forwards the information required
    to display the current challenge.
    """
    cursor = list(mongo.db.challenges.find({"_id": ObjectId(challenge)}))
    return render_template('game.html', challenge=cursor)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
