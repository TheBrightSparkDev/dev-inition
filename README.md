# [Word VS](http://word-vs.herokuapp.com/)

Link to site [Word VS](http://word-vs.herokuapp.com/)

Word Vs is basically wordle with friends you challenge your friends to guess your word very simple lots of fun.
The inspiration for this mostly came from the idea behind wordle one man wanted to challenge his wife everyday.
So with the app anyone can challenge anyone everyday or even more than once everyday!

<img src="responsive image" alt= "image of the website on various devices to show responsiveness" width="100%">

# Table of contents

1. [User stories](#Features)
 - [Main menu](#main_menu)
 - [Sign-in/Sign-up](#signin)
 - [Profile](#profile)
 - [Challenge a friend](#challenge_a_friend)
 - [Challenges page](#challenges_page)
 - [Sent challenges](#sent_challenges)
 - [Freeplay](#freeplay)
 - [Add friend](#add_friend)
 - [Game page](#game_page)
2. [Wireframes](#wireframes)
 - [interactive](#interactive)
3. [Challenges](#challenges)
 - [How many guess boxes?](#challenge1)
 - [Database troubles](#challenge2)
 - [Last guess gone!](#challenge3)
 - [Why won't you break?](#challenge4)
4. [Technology used](#technology_used)

desktop and background credit: [pixabay](https://pixabay.com/photos/apple-computer-desk-workspace-1868496/)

## User stories<a name="Features">

- __Main menu__<a name="main_menu">

 - The main menu contains a few links to sign in sign up or guest mode.
 - This allows people to sign up sign in or just try out the game to see if they like it

![Main menu](assets/images/main-menu.PNG)

- __Sign in/sign up page__<a name="signin">
 - Both pages are extremely similar one adds a new user to the database if they dont already exist the other
 checks username and password match an already existing user.
 - This is to allow users to get into the advanced features of the game like challenging friends and seeing challenges
 that hae been sent your way.


![Sign in](assets/images/game-screen.PNG)
![Sign up](assets/images/game-screen.PNG)

- __Profile__<a name="profile">

- This is the first page you see when youre logged in, it looks different based on whether youre logged in or not.
To users that are logged in it will display all the available options: challenges, sent challenges, challenge a friend 
and freeplay. For users that are logged in as guest the only option they will have is freeplay.
- Freeplay gives users the opportunity to try before they sign up if they arent sure about whether they will like the game.
![Profile](assets/images/tutorial.PNG)

- __Challenge a friend__<a name="challenge_a_friend">

- this is where you go to send your friends a challenge the first page you get to when you click the link off the profile is a friend picker. You first choose what friend you want to send the challenge to. Then you set the challenge the word needs to be valid and part of my database I've gathered of 48000 + words. This stops people from using bad words and making up words as that would ruin the game.

![Friend picker](assets/images/pause.PNG)
![Challenge set page](assets/images/pause.PNG)

- __Challenges Page__<a name="challenges_page">

- This is where you see challenges you've recieved from others.
- This allows users to complete challenges other users have sent them.

![Challenges](assets/images/game-over.PNG)

- __Sent challenges__<a name="sent_challenges">

- This page allows you to view and edit challenges you've sent to others and see if the person managed to complete the challenge or fail.
- This allows a user to edit the challenge they've sent if they arent happy with the word they sent off origionally it however doesnt allow the word to be edited if the challenge has been started. You may also delete challenges sent aswell.

![Sent challenges](assets/images/highscore.PNG)

- __Freeplay__<a name="freeplay">
  
 - This is a few levels that I have created this allows players to get an idea of what the game is like and wither they like it.

![Freeplay](assets/images/suggestions.PNG)

- __Add friend__<a name="add_friend">
  
- This is where users go to add friends. If youre only just signing in please feel free to add thebrightspark which is my profile and challenge me! 
- Users will be able to add eachother here. It only allows you to add users that exist.

![Add friend](assets/images/colorblind.PNG)

- __Game page__<a name="game_page">

- This is the main game where users will guess the words and they will display above the inout line in a grid you only have six guesses so mak sure they are good ones! Once you hit the guess limit its game over.
- Users will be able to complete challenges their friends sent them here or complete the freeplay levels.

# Wireframes<a name="wireframes">

### adobe XD<a name="interactive">

[interactive wireframe](https://xd.adobe.com/view/5fb66345-d813-4c0c-a24d-a927b8edc2d9-0ae5/)

This is the best way other than using the site to get an idea of how everything works

# Challenges overcome 

## How many game boxes??<a name="challenge1">

### Goal

Displaying the correct amount of boxes on the game screen and the guesses to display and change the box background if the letter was in the right spot

### Issue

The correct amount of boxes relies on the html page knowing how many letters are in the word getting that info wasnt straight forward initially as I had no idea how to do it. 

It also relied on the html page knowing that the letter was in the right place and what the correct answer was without displaying it to the user

### How I did it

After looking back at previous mini project: task manager I noticed we used |length to find the length of a word which solved the first problem

next was the conditional formatting of the box it sits in the way I implemented this was by using loop.index0 to check the letters of both the guess and the answer match and then also used the in keyword in jinja to check if the letter was part of the word string. If the letter was in the correct place it adds the class correct if not it moves on to checking if its in the word if it is a letter included in the word it adds the class nearly otherwise it just displays the same color as normal.

## Database troubles<a name="challenge2">

### Goal

To get the words onto the database

### Issue

I had a dictionary of 100k plus words varying in length and some even inclding special characters like "-" so the goal was to filter those out and only send over words between 5-8 letters long.

I didnt have time to do this manually

### How I did it

I created an app to iterate over the 100k words filter out any that include "-" and only send over the words if the length is '>' 4 and '<' 9 it took about 30 mins but when it was done I had 48k words and their definitions added to the mongo db database.

## Last guess gone!<a name="challenge3">

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

## Why won't you break!<a name="challenge4">

### Goal

get keyboard to stop functioning after the correct answer was submitted

### Issue

I have to kill to javascript functions in order to do this but javascript is unaware what the correct answer is so I cant just check to see if the correct answer is displayed

### How I did it

Theory: If I add some condtional formatting to the html form to check if challenge.word == challenge.guess then I should be able to add an attribute to something so java knows if the correct answer has been guessed to use this to destroy the keyboard functionality I could set currentInputBox to a word string like completed then incrementing it or decreasing it by 1 would be impossible and therefore stop the game working and most importantly stopping the user submitting more answers and triggerring a gameover event by accident.

Theory above was absolutely correct and works perfectly.

# Technology used<a name="technology_used">
## wireframes
- adobe XD
## Frameworks
- I used github to store the repository and version management
- I used gitpod for editing the code and for posting to github 
## Libraries
- no libraries used

# user story 

The users will be people just looking to relax and play something simple and fun. No minimum requirements and accessible from all devices too so users will be all kinds of people on all kinds of devices.

### Features Left to Implement

- free play mode

## Testing 


### big bugs

## bug tester Sharron
 - found a bug where you cannot add users that have a number in their name simply by creating a user name with a number in it that I couldnt add via app

### small bugs

## bug tester Rhi found:
 - display bug on challenges page back and no challenges found were displaying badly on the page
 - also spotted a spelling mistake on the add words page


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

- The site was deployed to GitHub pages. The steps to deploy are as follows:
  - In the GitHub repository, navigate to the Settings tab
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.
  - Make sure to select root before saving.

- The site was deployed to GitHub pages. 

The live link can be found here - [Word Vs]()


## Credits 

Below are the sources of all the media and content 

### Almost no parts of the code on this website are copy and pasted 

- If I was struggling with anything I would simply go to website that I have linked below and read up on how to use the specific code and then I would simply use the code correctly. 
- all websites used are linked below:
- [google fonts](https://fonts.google.com/)
- Code Institute mentor also sent me a link to a template of a README.md to create a structure I changed everything and kept structure apart from the steps to deploy as there isn't anything to change added a bit about making sure it was root as docs brings up an error message for me saying failed to build.

### Content 



### Media

 # More coming soon! 
 
 ### Follow me on github to stay upto date and message me for project ideas/pitches always ready to work with someone.
 
 # To do 
 only started noting things when I noticed I started forgetting things
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
## not done yet
 - need to make sure noone other than admin can get into the admin page
 - The only page an admin has easy access to is the add words and add words admin page
# small bug fixes
### backspace bug fix
 - the backspace doesn't delete the last letter on the currentWord variable which means the word either gets submmitted early after backspace or is a word that containns all the things you backspaced out the behaviour is only present in the keyboard controls and not the touch screen controls 
 - bug was fixed by slicing currentWord (0,-1) which takes only the last letter off the word and reassigning the value to itself so currentWord = currentWord.slice(0,-1) 
