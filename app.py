"""
controls the flow through the Word VS website and displays pages and
controls logic for most pages with assistance from the script.js file and
deleteitem.js file
"""
# imports all relevant assets
import os
from datetime import datetime
from flask import (
     Flask, flash, render_template,
     redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
# this import is used regardless of the error message
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
# sets the permanent environ variables
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
ADMIN_REAL = os.environ.get("ADMIN_REAL")
mongo = PyMongo(app)


@app.route("/")
def homepage():
    """
    displays the homepage allows users to sign in sign up or log in as guest
    This is also where you get sent if you page 404 and click the link to
    get back to safety so it does an additional check to make sure if the
    user is already signed in to direct them to their profile page instead.
    """
    if 'user' in session:
        return render_template("profile.html")
    return render_template("homepage.html")


# sign up section
@app.route("/signup", methods=["GET", "POST"])
def signup():
    """
    displays signup page and allows new users to create an acount to use the
    application
    """

    if request.method == "POST":
        # check if username in form element already exists in the database
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
    displays sign in and allows users to sign in to an account they
    have already created
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
                flash(f"welcome, {session['user']}")
                if session['user'] == ADMIN_REAL:
                    session['user'] = "admin"
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
    flash("See you again soon!")
    session.pop("user")
    return redirect(url_for("homepage"))


# profile section
@app.route("/profile/")
def profile():
    """
    displays profile and allows users to acces the sent_challenges
    page the challenges page and the challenge_a_friend page
    also (when implemented) will allow users to access the
    freeplay page
    """
    # checks if user is in session if they arent they must be guest
    if "user" in session:
        name = session['user']
    else:
        name = "guest"
        flash("It's more fun when you sign in")
    return render_template("profile.html", user=name)


@app.route("/friend_picker")
def friend_picker():
    """
    displays friend picker page which allows users to choose what friend
    on their friend list that they would like to challenge. It also
    shows user what other users have added them and allows them to
    accept the friend request
    """
    # checks if user is in session if not displays custom error message
    if "user" not in session:
        return render_template(
            "oops.html",
            message="You can't create a challenge without being logged in!",
            advice="Either sign in or sign up",
            links=['signin', 'signup']
            )
    # creates relevant variables
    current_user = session["user"].lower()
    requests = mongo.db.users.find({"friends": current_user})
    user = mongo.db.users.find_one({"username": current_user})
    friends = user["friends"]
    displayed_requests = []
    # removes users already on friendslist
    for user in requests:
        if user["username"] not in friends:
            displayed_requests += [user["username"]]
    return render_template(
        'friend_picker.html', friends=friends, requests=displayed_requests)


@app.route("/add_button/<username>")
def add_button(username):
    """
    displays friend picker page allows the user to add the friend that added
    them back otherwise funcitons just like the page above
    """
    # checks if user is in session
    if "user" not in session:
        return render_template(
            "oops.html",
            message="You can't add a friend without being logged in!",
            advice="Either sign in or sign up",
            links=['signin', 'signup']
            )
    # creates relevant variables
    add_user = username
    current_user = session["user"].lower()
    user = mongo.db.users.find_one({"username": current_user})
    friends = user["friends"]
    # adds user to friends list
    if username not in friends:
        mongo.db.users.update_many(
            {'username': session['user']},
            {'$push': {"friends": add_user}})
        flash("Friend added")
    else:
        flash("You are already friends")
    requests = mongo.db.users.find({"friends": current_user})
    displayed_requests = []
    # this is so page displays correctly when just refreshed
    real_friends = friends
    # removes the users that you already have on your friendslist
    # also corrects the friends and displayed requests to display correctly
    for user in requests:
        if user["username"] not in friends:
            displayed_requests += [user["username"]]
            if username in displayed_requests:
                displayed_requests.remove(username)
                real_friends = friends + [username]
    return render_template(
        'friend_picker.html',
        friends=real_friends,
        requests=displayed_requests)


@app.route("/add_friend", methods=["GET", "POST"])
def add_friend():
    """
    displays add_friend page and allows user to enter a username to add
    to their friends list the system checks if user exists and if they do
    it sends a request to the other user to see if they are happy to be
    added and confirm they are friends
    """
    # Checks user is in session if not displays custom error message
    if "user" not in session:
        return render_template(
            "oops.html",
            message="You can't adda friend without being logged in!",
            advice="Either sign in or sign up",
            links=['signin', 'signup']
            )
    # creates relevent variables
    add_user = request.form.get("username")
    user = mongo.db.users.find_one({"username": session['user'].lower()})
    friends = user["friends"]
    test = mongo.db.users.find_one({"username": add_user})
    # handles post method and displays feedback
    if request.method == "POST":
        if test is not None:
            if request.form.get("username") != session['user']:
                if request.form.get("username") not in friends:
                    mongo.db.users.update_many(
                        {'username': session['user']},
                        {'$push': {"friends": add_user}})
                    flash("Friend added")
                else:
                    flash("You are already friends")
            else:
                flash("You can't add yourself!")
        else:
            flash("User doesn't exist")
    return render_template('add_friend.html', friends=friends)


@app.route("/create_challenge/<friend>", methods=["GET", "POST"])
def create_challenge(friend):
    """
    displays create challenge page and allows users to challenge
    their friend the friend recieving the challenge must've added
    the user creating the challenge otherwise it will throw an
    error page called oops.html with a custom error message
    on what went wrong.
    Also sends a challenge to the database
    """
    # defensive programming to check if user is logged in
    if "user" not in session:
        return render_template(
            "oops.html",
            message="You can't create a challenge without being logged in!",
            advice="Either sign in or sign up",
            links=['signin', 'signup']
            )
    # if user doesn't match the "for" in the challenge redirects to oops
    check = mongo.db.users.find_one({"username": friend})
    checklist = check.get("friends")
    user = session['user']
    i = 0
    for name in checklist:
        if name == session['user']:
            i = i + 1
            break
    if i == 0:
        return render_template(
            "oops.html",
            message=f"You're not on {friend}'s friendlist",
            advice=f"Tell them to add your username: {user}",
            links=['home', 'back']
            )

    mongo.db.users.find_one({"username": friend})
    if request.method == "POST":
        now = datetime.now()
        format_now = now.strftime("%d/%m/%Y %H:%M:%S")
        word = request.form.get("word").lower()
        letters = request.form.get("letters").lower()
        check = mongo.db.wordlist.find_one({"word": word})
        for letter in word:
            if letter not in letters:
                letters = letters + letter
        letters = "".join(set(letters))
        try:
            # this throws an error if word isnt in database forcing system to
            # skip to except
            word_check = check.get("word")
            challenge = {"for": friend,
                         "word": word,
                         "letters": letters,
                         "from": session['user'],
                         "state": "created",
                         "created_date": format_now,
                         "updated_date": format_now,
                         "guess_1": "",
                         "guess_2": "",
                         "guess_3": "",
                         "guess_4": "",
                         "guess_5": "",
                         "guess_6": "",
                         }
            mongo.db.challenges.insert_one(challenge)
            flash("challenge sent")
        except AttributeError:
            flash("Invalid word")
    return render_template('create_challenge.html', friend=friend)


@app.route("/challenges")
def challenges():
    """
    displays the challenges that have been sent to the user the
    page also checks if user is in session as if they are not the
    page will not work and it will break as it relies on the
    session['user'] cookie to function if user is not in session
    the page will display as oops.html with a custom error message
    """
    # checks if user is not in session
    if "user" not in session:
        return render_template(
            "oops.html",
            message="You can only see challenges if logged in",
            advice="Either sign in or sign up",
            links=['signin', 'signup']
            )
    # if user is in session this retrieves challenges sent to them
    user = session['user']
    challenges_list = list(mongo.db.challenges.find({"for": user}))
    return render_template('challenges.html', challenges=challenges_list)


@app.route("/give_up/<challenge_id>")
def give_up(challenge_id):
    """
    Gives up on challenge this is a way of clearing challenges that you
    don't want to do or are struggling with first it checks if user is in
    session and then executes the code that changes the state of the
    challenge to quit
    """
    # checks if user in not in session
    if "user" not in session:
        return render_template(
            "oops.html",
            message="You can only see challenges if logged in",
            advice="Either sign in or sign up",
            links=['signin', 'signup']
            )
    # if user is in session executes the code to change the state to quit
    query = {"_id": ObjectId(challenge_id)}
    mongo.db.challenges.update_one(query, {"$set": {"state": "quit"}})
    user = session['user']
    challenges_list = list(mongo.db.challenges.find({"for": user}))
    return render_template('challenges.html', challenges=challenges_list)


@app.route("/sent_challenges")
def sent_challenges():
    """
    displays the challenges sent by an individual it also allows the
    individual to change the challenge they've sent sent challenges are
    put into different categories depending on their state if their state
    is completed or quit the user gets to delete them if the state is edit
    the page corrects it to created as clearly the user has abandoned their
    last attempt to edit. you can also see the persons guesses and when they
    last attempted the challenge
    """
    # checks if user is not in session
    if "user" not in session:
        return render_template(
            "oops.html",
            message="You can't check sent challenges without being logged in!",
            advice="Either sign in or sign up",
            links=['signin', 'signup']
            )
    # this is simply to make the for loop work later on both python and jinja
    guesses = [
        "guess_1", "guess_2", "guess_3", "guess_4", "guess_5", "guess_6"]
    user = session['user']
    challenges_list = mongo.db.challenges.find({"from": user})
    # iterates through the list and checks if state is editing
    for challenge in challenges_list:
        # if state is in editing it changes it back to created
        if challenge.get("state") == "editing":
            query = {"_id": ObjectId(challenge.get("_id"))}
            submit = {"$set": {"state": "created"}}
            mongo.db.challenges.update_one(query, submit)
    # had to get it again due to the previous cursor being consumed
    challenges_list = list(mongo.db.challenges.find({"from": user}))
    return render_template(
        'sent_challenges.html', challenges=challenges_list, guesses=guesses)


@app.route("/edit_challenge/<friend>/<challenge_id>", methods=["GET", "POST"])
def edit_challenge(friend, challenge_id):
    """
    displays edit challenge page and stops users being able to access the
    challenge while its being edited this is to avoid confusion users will
    only be able to edit challenges that havent been started yet only
    also sends a challenge to the database
    """
    # defensive programming to check if user is logged in
    if "user" not in session:
        return render_template(
            "oops.html",
            message="You can't create a challenge without being logged in!",
            advice="Either sign in or sign up",
            links=['signin', 'signup']
            )
    # if user doesn't match the "for" in the challenge redirects to oops
    check = mongo.db.users.find_one({"username": friend})
    checklist = check.get("friends")
    user = session['user']
    # this declares a variable for the for loop
    i = 0
    # this checks all names is in the checklist
    for name in checklist:
        # if name matches the current user
        if name == session['user']:
            # it increments i by one
            i = i + 1
            break
    # so if i was incremented it means that you are on the users friends list
    if i == 0:
        # this runs if user isnt on the friendslist
        return render_template(
            "oops.html",
            message=f"You're not on {friend}'s friendlist",
            advice=f"Tell them to add your username: {user}",
            links=['home', 'back']
            )

    mongo.db.users.find_one({"username": friend})
    challenge = mongo.db.challenges.find_one({"_id": ObjectId(challenge_id)})
    # Checks if the challenge has been started
    if "started" == challenge.get("state"):
        return render_template(
            "oops.html",
            message="The challenge has been started already",
            advice="go back to the profile page",
            links=['home']
            )
    query = {"_id": ObjectId(challenge_id)}
    mongo.db.challenges.update_one(query, {"$set": {"state": "editing"}})
    # handles te post method
    if request.method == "POST":
        # declares important variables
        now = datetime.now()
        format_now = now.strftime("%d/%m/%Y %H:%M:%S")
        word = request.form.get("word").lower()
        letters = request.form.get("letters").lower()
        check = mongo.db.wordlist.find_one({"word": word})
        query = {"_id": ObjectId(challenge_id)}
        # this makes sure theres no duplicates in the letters
        for letter in word:
            if letter not in letters:
                letters = letters + letter
        letters = "".join(set(letters))
        try:
            # this throws an AttributeError if word isnt in database
            word_check = check.get("word")
            challenge = {"$set": {
                         "for": friend,
                         "word": word,
                         "letters": letters,
                         "from": session['user'],
                         "state": "created",
                         "updated_date": format_now
                         }}
            mongo.db.challenges.update_one(query, challenge)
            flash("challenge edited")
        # this catches the AttributeError
        except AttributeError:
            flash("Invalid word")
    return render_template(
        'edit_challenge.html',
        challenge=challenge_id,
        friend=friend)


@app.route("/delete_challenge/<challenge_id>")
def delete_challenge(challenge_id):
    """
    deletes a challenge when delete button is pressed on the sent challenges
    page
    """
    # this is the code that deletes the challenge
    if request.method == "GET":
        mongo.db.challenges.delete_one({"_id": ObjectId(challenge_id)})
        flash("deleted challenge")
    # these are the variables that sent_challenges needs to display correctly
    guesses = [
        "guess_1", "guess_2", "guess_3", "guess_4", "guess_5", "guess_6"]
    user = session['user']
    challenges_list = list(mongo.db.challenges.find({"from": user}))
    return render_template(
        "sent_challenges.html", challenges=challenges_list, guesses=guesses)


@app.route("/game/<challenge>", methods=["GET", "POST"])
def game(challenge):
    """
    displays the main game and forwards the information required
    to display the current challenge.
    """
    # checks if user is logged in if not sends the to the oops page
    if "user" not in session:
        return render_template(
            "oops.html",
            message="You're not signed in",
            advice="Either sign in or sign up",
            links=['signin', 'signup']
            )
    # this gathers the information from the database as a cursor
    cursor = list(mongo.db.challenges.find({"_id": ObjectId(challenge)}))
    challenge_to_update = mongo.db.challenges.find_one(
                {"_id": ObjectId(challenge)})
    # I wanted to create a dictionary so it was easier to manage
    data = {}
    for i in cursor:
        data.update(i)
    print(data)
    # This is relevant later on it is here as to keep code DRY
    query = {"_id": ObjectId(challenge)}
    # if user doesn't match the "for" in the challenge it redirects to oops
    user = session['user']
    check = mongo.db.challenges.find_one({"username": user})
    # Checks if the challenge is actually for current user
    if user != data.get("for"):
        return render_template(
            "oops.html",
            message="This challenge isn't for you or has been deleted",
            advice="Either sign in, sign up or go back to the profile page",
            links=['signin', 'signup', 'home']
            )
    # Checks if the challenge has been quit
    if "quit" == data.get("state"):
        return render_template(
            "oops.html",
            message="You already gave up on this challenge!",
            advice="go back to the profile page",
            links=['home']
            )
    # Checks if challenger is editing
    if "editing" == data.get("state"):
        return render_template(
            "oops.html",
            message="The person that sent this challenge is editing it please wait",
            advice="go back to the profile page",
            links=['home']
            )
    # This sets the state to created so that the creator cannot edit it
    if challenge_to_update.get("state") == "created":
        mongo.db.challenges.update_one(query, {'$set': {"state": "started"}})
    correct = data.get("word")
    # this is so that I can use a for loop on the quesses
    guesses = [
            "guess_1", "guess_2", "guess_3", "guess_4", "guess_5", "guess_6"]
    # handles the post method
    if request.method == "POST":
        word = request.form.get("answer")
        check = mongo.db.wordlist.find_one({"word": word})
        now = datetime.now()
        format_now = now.strftime("%d/%m/%Y %H:%M:%S")
        try:
            # this throws an AttributeError if word isnt in database
            word_check = check.get("word")
            # this checks if word was the correct word
            if word == correct:
                # this checks for the first empty guess in guesses
                for guess in guesses:
                    # if guess is empty it adds the most recent guess
                    if challenge_to_update.get(guess) == "":
                        submit = {"$set": {guess: word}}
                        dict_update = {guess: word}
                        data.update(dict_update)
                        mongo.db.challenges.update_one(query, submit)
                        # this changes state to completed
                        mongo.db.challenges.update_one(
                            query, {'$set': {"state": "completed"}})
                        # this updates the time it was last updated
                        mongo.db.challenges.update_one(
                            query, {"$set": {"updated_date": format_now}})
                        flash("Correct, Well done")
                        break
                        # this checks if the guess has already been guessed
                    elif challenge_to_update.get(guess) == word:
                        flash("Already guessed")
                        break
            else:
                # this runs if the guess is wrong
                for guess in guesses:
                    # this looks for the first empty guess
                    if challenge_to_update.get(guess) == "":
                        submit = {"$set": {guess: word}}
                        dict_update = {guess: word}
                        data.update(dict_update)
                        mongo.db.challenges.update_one(query, submit)
                        # this updates the updated date
                        mongo.db.challenges.update_one(
                            query, {"$set": {"updated_date": format_now}})
                        break
                    # this checks if guess has already been guessed
                    elif challenge_to_update.get(guess) == word:
                        flash("Already guessed")
                        break
        # handles the AttributeError
        except AttributeError:
            flash("Invalid word")
    letters = ""
    # this makes a list of all the letters that are in previous guesses
    for guess in guesses:
        guess_check = data[guess]
        for letter in guess_check:
            letters = letters + letter
    # this removes duplicate letters
    used = "".join(set(letters))

    return render_template(
        'game.html', challenge=data, guesses=guesses, used=used)


@app.route("/add_words/<referrer>/<key>", methods=["GET", "POST"])
def add_words(referrer, key):
    """
    Allows users to add words to the word database referrer and key
    allow me to send them straight back to where they were referrer
    indicates what page they came from (game or create_challenge) the
    key is either the friends name from create_challenge or the
    challenge._id from game words added here don't go to the main
    database only to a suggestions database where an admin can review
    the word and definition
    """
    # checks if user is in session
    if "user" not in session:
        return render_template(
            "oops.html",
            message="You're not signed in",
            advice="Either sign in or sign up",
            links=['signin', 'signup']
            )
    if request.method == "POST":
        # check if word in form element exists already in the database
        existing_word = mongo.db.wordlist.find_one(
            {"word": request.form.get("word").lower()})
        if existing_word:
            flash("This word is already in the database")
        else:
            existing_word = mongo.db.new_words.find_one(
                {"word": request.form.get("word").lower()})
            if existing_word:
                flash("This word has already been suggested")
            else:
                # if word is new adds it to suggestions database
                new_word = {
                    "word": request.form.get("word"),
                    "meaning": request.form.get("definition")
                    }
                mongo.db.new_words.insert_one(new_word)

    return render_template("add_words.html", referrer=referrer, key=key)


@app.route("/add_words_admin", methods=["GET", "POST"])
def add_words_admin():
    """
    Allows admin to add words to the in use database the admin
    will be able to review words sent in and accept them admin is
    determined in the app.config file which is hidden from the
    public. The admins username is also not admin and the admin
    username has been reserved on the database to prevent someone
    calling themselves admin the reason I create a form for each
    word is so I can very easily edit the word or definition
    """
    # checks if user is in session
    if "user" not in session:
        return render_template(
            "oops.html",
            message="You're not signed in",
            advice="Either sign in or sign up",
            links=['signin', 'signup']
            )
    # checks if user is not an admin
    if session['user'] != "admin":
        return render_template(
            "oops.html",
            message=(
                "This page is not for users"),
            advice="Please don't try this again",
            links=['home']
            )
    # handles the POST method
    if request.method == "POST":
        # check if word in form element exists already in the database
        existing_word = mongo.db.wordlist.find_one(
            {"word": request.form.get("word").lower()})
        if existing_word:
            flash("This word is already in the database")
        else:
            word = request.form.get("word")
            new_word = {
                "word": word.lower(),
                "meaning": request.form.get("definition")
                }
            mongo.db.wordlist.insert_one(new_word)
            mongo.db.new_words.delete_one({"word": word})
            flash("Updated database")
    # this is for display purposes only
    words = mongo.db.new_words.find()
    amount = len(list(mongo.db.new_words.find()))

    return render_template("add_words_admin.html", words=words, amount=amount)


@app.errorhandler(404)
def page_not_found(e):
    """
    note that we set the 404 status explicitly
    """
    return render_template('404.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
