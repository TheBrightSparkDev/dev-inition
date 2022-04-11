# [Word VS](http://word-vs.herokuapp.com/)

Link to site [Word VS](http://word-vs.herokuapp.com/)

Word Vs is basically wordle with friends you challenge your friends to guess your word very simple lots of fun.
The inspiration for this mostly came from the idea behind wordle one man wanted to challenge his wife everyday.
So with the app anyone can challenge anyone everyday or even more than once everyday!

<img src="responsive image" alt= "image of the website on various devices to show responsiveness" width="100%">

# Table of contents
1. [User stories](#user_stories)
2. [Features](#Features)
 - [Main menu](#main_menu)
 - [Sign-in/Sign-up](#signin)
 - [Profile](#profile)
 - [Challenge a friend](#challenge_a_friend)
 - [Challenges page](#challenges_page)
 - [Sent challenges](#sent_challenges)
 - [Freeplay](#freeplay)
 - [Add friend](#add_friend)
 - [Game page](#game_page)
3. [Wireframes](#wireframes)
 - [interactive](#interactive)
4. [Challenges](#challenges)
 - [How many guess boxes?](#challenge1)
 - [Database troubles](#challenge2)
 - [Last guess gone!](#challenge3)
 - [Why won't you break?](#challenge4)
5. [Technology used](#technology_used)
 - [wireframe](#wireframe)
 - [frameworks](#frameworks)
 - [libraries](#libraries)
6. [features left to implement](#features-left-to-implement)
6. [testing](#testing)
 - [homepage.html](#homepage.html)
 - [signin.html](#signin.html)
 - [signup.html](#signup.html)
 - [profile.html](#profile.html)
 - [sent_challenges.html](#sent-challenges.html)
 - [add_friends.html](#add-friends.html)
 - [add_words admin.html](#add-words-admin.html)
 - [add_words.html](#add-words.html)
 - [base.html](#base.html)
 - [challenges.html](#cahllenges.html)
 - [create_challenges.html](#create-challenges.html)
 - [edit_challenges.html](#edit-challenges.html)
 - [friend_picker.html](#friend-picker.html)
 - [game.html](#game.html)
 - [oops.html](#oops.html)

desktop and background credit: [pixabay](https://pixabay.com/photos/apple-computer-desk-workspace-1868496/)

## User stories <a name="user_stories">

## Features<a name="Features"></a>

- __Main menu__<a name="main_menu"></a>

 - The main menu contains a few links to sign in sign up or guest mode.
 - This allows people to sign up sign in or just try out the game to see if they like it

![Main menu](assets/images/main-menu.PNG)

- __Sign in/sign up page__<a name="signin"></a>
 - Both pages are extremely similar one adds a new user to the database if they dont already exist the other
 checks username and password match an already existing user.
 - This is to allow users to get into the advanced features of the game like challenging friends and seeing challenges
 that hae been sent your way.


![Sign in](assets/images/game-screen.PNG)
![Sign up](assets/images/game-screen.PNG)

- __Profile__<a name="profile"></a>

- This is the first page you see when youre logged in, it looks different based on whether youre logged in or not.
To users that are logged in it will display all the available options: challenges, sent challenges, challenge a friend 
and freeplay. For users that are logged in as guest the only option they will have is freeplay.
- Freeplay gives users the opportunity to try before they sign up if they arent sure about whether they will like the game.
![Profile](assets/images/tutorial.PNG)

- __Challenge a friend__<a name="challenge_a_friend"></a>

- this is where you go to send your friends a challenge the first page you get to when you click the link off the profile is a friend picker. You first choose what friend you want to send the challenge to. Then you set the challenge the word needs to be valid and part of my database I've gathered of 48000 + words. This stops people from using bad words and making up words as that would ruin the game.

![Friend picker](assets/images/pause.PNG)
![Challenge set page](assets/images/pause.PNG)

- __Challenges Page__<a name="challenges_page"></a>

- This is where you see challenges you've recieved from others.
- This allows users to complete challenges other users have sent them.

![Challenges](assets/images/game-over.PNG)

- __Sent challenges__<a name="sent_challenges"></a>

- This page allows you to view and edit challenges you've sent to others and see if the person managed to complete the challenge or fail.
- This allows a user to edit the challenge they've sent if they arent happy with the word they sent off origionally it however doesnt allow the word to be edited if the challenge has been started. You may also delete challenges sent aswell.

![Sent challenges](assets/images/highscore.PNG)

- __Freeplay__<a name="freeplay"></a>
  
 - This is a few levels that I have created this allows players to get an idea of what the game is like and wither they like it.

![Freeplay](assets/images/suggestions.PNG)

- __Add friend__<a name="add_friend"></a>
  
- This is where users go to add friends. If youre only just signing in please feel free to add thebrightspark which is my profile and challenge me! 
- Users will be able to add eachother here. It only allows you to add users that exist.

![Add friend](assets/images/colorblind.PNG)

- __Game page__<a name="game_page"></a>

- This is the main game where users will guess the words and they will display above the inout line in a grid you only have six guesses so mak sure they are good ones! Once you hit the guess limit its game over.
- Users will be able to complete challenges their friends sent them here or complete the freeplay levels.

# Wireframes<a name="wireframes"></a>

### adobe XD<a name="interactive"></a>

[interactive wireframe](https://xd.adobe.com/view/5fb66345-d813-4c0c-a24d-a927b8edc2d9-0ae5/)

This is the best way other than using the site to get an idea of how everything works

# Challenges overcome 

## How many game boxes??<a name="challenge1"></a>

### Goal

Displaying the correct amount of boxes on the game screen and the guesses to display and change the box background if the letter was in the right spot

### Issue

The correct amount of boxes relies on the html page knowing how many letters are in the word getting that info wasnt straight forward initially as I had no idea how to do it. 

It also relied on the html page knowing that the letter was in the right place and what the correct answer was without displaying it to the user

### How I did it

After looking back at previous mini project: task manager I noticed we used |length to find the length of a word which solved the first problem

next was the conditional formatting of the box it sits in the way I implemented this was by using loop.index0 to check the letters of both the guess and the answer match and then also used the in keyword in jinja to check if the letter was part of the word string. If the letter was in the correct place it adds the class correct if not it moves on to checking if its in the word if it is a letter included in the word it adds the class nearly otherwise it just displays the same color as normal.

## Database troubles<a name="challenge2"></a>

### Goal

To get the words onto the database

### Issue

I had a dictionary of 100k plus words varying in length and some even inclding special characters like "-" so the goal was to filter those out and only send over words between 5-8 letters long.

I didnt have time to do this manually

### How I did it

I created an app to iterate over the 100k words filter out any that include "-" and only send over the words if the length is '>' 4 and '<' 9 it took about 30 mins but when it was done I had 48k words and their definitions added to the mongo db database.

## Last guess gone!<a name="challenge3"></a>

### Goal

get the page to display the guesses correctly

### Issue

Upon submit the HTML page refreshes this causes the page to rebuild and send off the info at the same time...
problem here is that the system requests the info down from the server which at this point hasnt recieved the new guess so the new guess isnt displayed... 

I submit the form using javascript and the refreshing of the page means I dont need to clear all the input boxes which is ideal. Saves me creating an extra function and am not aware of a way of sending info from a html page to python without submitting

Also upon manual refreshing it sends the same guess through again which means refreshing the page again after a second delay is not an option

### How I did it

I sent the guess back to the HTML page via python I had to first of all add some if statements to check if any of the guesses had already been guessed then I would create a new dict that included the guess at the correct line. 

There is a small bug left here though if you manage to guess twice in less than 500ms it can cause and issue where the first guess is lost but doing this is very difficult and extremely unlikely.

I also got the python app to check if the guess had already been guessed and blocked it if it had. 
This lead to a lengthy function but it worked so thats all that mattered.

## Why won't you break!<a name="challenge4"></a>

### Goal

get keyboard to stop functioning after the correct answer was submitted

### Issue

I have to kill to javascript functions in order to do this but javascript is unaware what the correct answer is so I cant just check to see if the correct answer is displayed

### How I did it

Theory: If I add some condtional formatting to the html form to check if challenge.word == challenge.guess then I should be able to add an attribute to something so java knows if the correct answer has been guessed to use this to destroy the keyboard functionality I could set currentInputBox to a word string like completed then incrementing it or decreasing it by 1 would be impossible and therefore stop the game working and most importantly stopping the user submitting more answers and triggerring a gameover event by accident.

Theory above was absolutely correct and works perfectly.

# Technology used<a name="technology_used"></a>
## wireframes<a name="wireframes"></a>
- adobe XD
## Frameworks<a name="frameworks"></a>
- I used github to store the repository and version management
- I used gitpod for editing the code and for posting to github 
## Libraries<a name="libraries"></a>
- no libraries used

### Features Left to Implement<a name="features-left-to-implement"></a>

- free play mode

## Testing <a name="testing"></a>

## individual pages

### Homepage.html <a name="homepage.html"></a>

The correct function is just a page for users to decide if they need to sign in or out has no other functionality other than that.

#### test cases

- Check all links
  - sign in, sign up and guest mode

### Signin.html <a name="signin.html"></a>

The correct function for this site is to allow the user to sign in if the user doesn't have log ins then there is a link to go to the signup page

#### test cases

- Check all links
  - word vs links to the homepage
  - signup page
- The page should allow only users with extisting account to log in.
- If the user doesnt exist it will redirect users to the sign up page
- If the user exists it will allow them to log in if the password is incorrect 
- The flash message should display the same message regardless of whether the password or the log in is incorrect

### signup.html <a name="signup.html"></a>

- The function of this page is to allow users to signup it doesnt differ much from the sign in page apart from the link at the bottom of the page is slightly different so the test cases are the same

#### test cases

- Check all links
  - word vs links to the homepage
  - signup page
- The page should allow only users without an extisting account to log in.
- If the user does exist it will redirect users to the sign in page
- Once the user submits it should load the profile page
- The flash message should display the same message regardless of whether the password or the log in is incorrect

### profile.html <a name="profile.html"></a>

- Usual functionality would be to display three different versions of itself one version for logged in users, one version to users that chose the guest option and another for the admin.

#### test cases

- Links to check 
  - Sent-challenges
  - Challenges
  - Challenge a friend
  - The word vs is also a link but links to profile
  - sign out - removes the user cookie and send user to the homepage

Ways to check all versions is to log in as admin/ a regular user and also clicking the guest option.

Unfortunately freeplay mode has not been added yet so that link is not active.

### sent_challenges.html <a name="sent-challenges.html"></a>

Normal functionality of this site is only to allow logged in users to use this site. Once a logged in user logs in it uses the session cookie's content to determine what challenges will be displayed. It should only display challenges that have been sent out by the current user. There are 4 different states that can be seen on this page created, started, completed and quit

#### test cases

- The links to check:
  - Back goes back to profile
  - Word vs links to profile
  - Each challenge has a link depending on it's state
  - Completed and quit have links to delete
  - Created challenges have a link to edit the challenge.
  - Started challenges shouldn't have any links.

### add_friends.html <a name="add-friends.html"></a>

Normal functionality of this page would be for a logged in user only to be able to add users that exist adding a user that doesnt exist should not be possible.

#### Test cases

- Links to check
  - add friend
  - back

The add friends button is a sumbit and it sends the username value to python to be checked if that user exists within the MongoDB database. This will display an error message if you add someone that doesnt exist.    

### add_words_admin.html <a name="add-words-admin.html"></a>

This page should not be accessible to regular users only one account has access to this so testing is impossible outside of development.
Regardless one way it can still be tested is by trying to access the page. Usual functionality would be to display all of the suggstions that users have made and allow you to accept them.

#### Test cases

links to check
- Word VS takes you back to the admin homepage
- Send button sends a suggestion to the mongoDB

The normal functionality is to send the word and definition from the word suggestion database to the word database. You can also add to the word or description currently there is no way to delete the suggestion other than on mongoDB currently so thats not a bug it's just yet to be implemented.

### add_words.html <a name="add-words.html"></a>

Normal functionality should be that this page should only be accessible by logged in users the users. The link to this page should only display when the user inputs a word that doesn't exist on either the challenge creation page or the game page. Depending on where you came from the back button will send you exactly where you came from. This is my way of making it easier for people to help out in developing the word base.

#### Test cases

links to check
- Word vs should take you to the profile page
- The back button should take you back where you came from.


### base.html <a name="base.html"></a>

This simply acts as a placeholder for the content of each site it also holds the links to the css file it doesn't do an awful lot sadly and cant really be visualised apart from the background because that technically does come from the base

#### test cases
- Best way to test if the base is displaying and working correctly is if the content is centered on the screen.
- Another way of checking it works is if anything on the screen has a style.
- The third of many other ways of checking is if the background is coloured blue and black in a linear gradient.
- It is very obvious if it's not working or displaying correctly

### challenges.html <a name="challenges.html"></a>

Usual behaviour is to display challenges that the current user has been sent by their friends. It displays differently depending on the state of the challenge. If the state is created it will go into the New challenges box. As soon as the challenge is started the challenge state changes to started. While the state is started the challenge goes into the already started box. The reason they are seperated is because the started state allows you to give up on the challenge. Whereas the challenges that haven't been attempted cannot be given up on. 

#### test cases

- links to test
  - Each challenge when clicked should take you to the game page for that particular challenge
  - Each challenge when started should allow you to press on a give up button. The give up button will remove the challenge from the list and the person who sent the challenge will be able to see you gave up or "quit" 
  - The word vs title should take you back to the profile.
  - The back button should also take you to the profile page.

- Try accessing the page while not logged in it should send you to oops.html
- Try to access a challenge that is currently being edited by the creator of the challenge it should stop the user from clicking on it.

### create_challenges.html <a name="create-challenges.html"></a>

Usual behaviour is to allow a user to send a challenge. Each create challenge page will be for a specific user. If there is no user selected the page will go through to the 404 page. If the user isn't in the database for example if you changed the name at the top of the page after create_challenges then it would send users to the oops.html page with a custom message. This is caught by a try except catch which if it is unable to find the user instead of crashing and saying it doesn't have a get method it instead displays the oops.html page.

#### test cases

- links to check
 - Send will send the challenge if the word is valid if not it will tell the user the word is invalid and give them the option to suggest the word
 - Back will go back to the friends list
 - word vs will as usual send you back to the profile page.

- Another way to try and challenge the page is to change the name in the web address to something different, change the name to a user thats not on the current users friends list and lastly removing the name altogether. The first two will give you oops.html the third will send you to 404.html.
- The last way to test the page is to click the link to suggest a word then on that page press back and it should send you back to create_challenge with the correct name in the address and any challenges sent should go to the intended user.

### edit_challenges.html <a name="edit-challenges.html"></a>

usual behaviour

#### test cases

### friend_picker.html <a name="friend-picker.html"></a>

usual behaviour

#### test cases

### game.html <a name="game.html"></a>

usual behaviour

#### test cases

### oops.html <a name="oops.html"></a>

usual behaviour

#### test cases

### 404.html <a name="404.html"></a>

The function of this page is to catch people who have manually typed in a bad address

#### Test cases

- type in a bad link 
- if the 404 page displays then it's working correctly
- 
### big bugs

## bug tester Rachel 
 - found a bug where if you add a space to the end of the create challenge page it doesnt allow you to send and reason is unclear
 - pointed out the rules are too small to see on a small screen
  - made font responsive

## bug tester Sharron
 - found a bug where you cannot add users that have a number in their name simply by creating a user name with a number in it that I couldnt add via app
  - removed validation rule to block numbers form add friends HTML page

### small bugs

## bug tester Rhi found:
 - display bug on challenges page back and no challenges found were displaying badly on the page
  - corrected by making div responsive (flexbox) and centered the back button by removing a misplaced div end tag
 - also spotted a spelling mistake on the add words page
  - characters was spelled charecters


### lighthouse Testing 


### Validator Testing 

# HTML
 ## index.html
  - No errors were returned when using the official [W3C validator]()
 ## suggestions.html
  - No errors were returned when using the official [W3C validator]()
# CSS
 ## style.css
  - No errors were found when using the official [(Jigsaw) validator]()
# JS
 ## script.js
 - No errors were found [JShint validator](https://jshint.com/)

### Unfixed Bugs

## Deployment

I was using github as the repository for the whole project so when I wanted to create a live page it was very easy to do.

- The site was deployed to Heroku. The steps to deploy are as follows:


## How to clone repository:
 - Go to my github repository [Word VS](https://github.com/TheBrightSparkDev/word-vs)
 -  Click the code option and then copy the link
 - if you have git installed on your pc you can use git clone followed by the URL 

- The site was deployed to heroku pages. 

The live link can be found here - [Word Vs](http://word-vs.herokuapp.com/)


## Credits 

Below are the sources of all the media and content 

Backspace button image created by me using adobe illustrator.

### Almost no parts of the code on this website are copy and pasted 

- If I was struggling with anything I would simply go to website that I have linked below and read up on how to use the specific code and then I would simply use the code correctly. 
- websites I copy and pasted from:
- [google fonts](https://fonts.google.com/)
- all websites used are linked below nothing was copy and pasted just checked:
- [Werkzeug security](https://werkzeug.palletsprojects.com/en/2.0.x/utils/)
- [Jinja cheatsheet](https://jinja.palletsprojects.com/en/3.0.x/templates/#variables)
- [Converting cursor to dict](https://stackoverflow.com/questions/28968660/how-to-convert-a-pymongo-cursor-cursor-into-a-dict)
- [How to add item to dict python](https://www.w3schools.com/python/python_dictionaries_add.asp)
- [Best way to make responsive text](https://www.w3schools.com/howto/howto_css_responsive_text.asp)
- [Changing the value of a form element](https://www.w3schools.com/howto/howto_css_responsive_text.asp)
- [How to get length of cursor](https://stackoverflow.com/questions/35692719/how-to-get-the-length-of-a-cursor-from-mongodb-using-python)
- Code Institute mentor also sent me a link to a template of a README.md to create a structure I changed everything and kept structure apart from the steps to deploy as there isn't anything to change added a bit about making sure it was root as docs brings up an error message for me saying failed to build.

### Content 



### Media

 # More coming soon! 
 
 ### Follow me on github to stay upto date and message me for project ideas/pitches always ready to work with someone.
 
 # To do 
 only started noting things when I noticed I started forgetting things
 - talk about the defensive programming of delete and give up return confirm("are you sure") worked but was an error in readme
## completed
  - make sure all pages go somewhere relevent when the title is clicked if title is present
  - create challenge needs to check if word is a word and if it is prevent it being sent
  - create challenge needs to make sure all the letters from the word are in letters
  - create challenge needs to make sure that all letters are unique
  - need to deploy page to heroku
  - user cant add self
  - user cant add user that doesnt exist
  - usernames are stored as lowercase only
  - cant use uppercase in username
  - add word page needs to be created needs to send words to a suggestion database also needs to check if word exists or not
  - add words admin needs to be created need to be able to see all suggestions and definitions and one click add to the wordlist database
  - delete function needs to be made for previous challenges page
  - edit function needs to be made for previous challenges page 
  - edit page also needs to change state to being updated but somehow revert it if the user cancels
  - need to make sure noone other than admin can get into the admin page
   - The only page an admin has easy access to is the add words and add words admin page
## not done yet
- change test cases on readme to this format:
  - how it should work 
  - how you can push it to see if it breaks 
- change code comments to this format
  - [Correct code docstring formats](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
- How to deploy via Heroku instructions including what variables you need to mention (not their values)
## freeplay mode
### words to note for potential freeplay levels
   - lashed
   - thyme
   - field
   - welded
   - phony
   - pushy
   - icycle
   
# small bug fixes
### backspace bug fix
 - the backspace doesn't delete the last letter on the currentWord variable which means the word either gets submmitted early after backspace or is a word that containns all the things you backspaced out the behaviour is only present in the keyboard controls and not the touch screen controls 
 - bug was fixed by slicing currentWord (0,-1) which takes only the last letter off the word and reassigning the value to itself so currentWord = currentWord.slice(0,-1) 
