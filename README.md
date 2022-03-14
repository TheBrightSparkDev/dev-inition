# [Word VS]()

Link to site [Word VS]()

Word Vs is basically wordle with friends you challenge your friends to guess your word very simple lots of fun.
The inspiration for this mostly came from the idea behind wordle one man wanted to challenge his wife everyday.
So with the app anyone can challenge anyone everyday or even more than once everyday!

<img src="responsive image" alt= "image of the website on various devices to show responsiveness" width="100%">

desktop and background credit: [pixabay](https://pixabay.com/photos/apple-computer-desk-workspace-1868496/)

## Features 

### The first menu

- __Main menu__

  - The main menu contains a few links to sign in sign up or guest mode.
  - This allows people to sign up sign in or just try out the game to see if they like it

![Main menu](assets/images/main-menu.PNG)

- __Sign in/sign up page__
 - Both pages are extremely similar one adds a new user to the database if they dont already exist the other
 checks username and password match an already existing user.
 - This is to allow users to get into the advanced features of the game like challenging friends and seeing challenges
 that hae been sent your way.


![Sign in](assets/images/game-screen.PNG)
![Sign up](assets/images/game-screen.PNG)

- __Profile__

- This is the first page you see when youre logged in, it looks different based on whether youre logged in or not.
To users that are logged in it will display all the available options: challenges, sent challenges, challenge a friend 
and freeplay. For users that are logged in as guest the only option they will have is freeplay.
- Freeplay gives users the opportunity to try before they sign up if they arent sure about whether they will like the game.
![Profile](assets/images/tutorial.PNG)

- __Challenge a friend__

- this is where you go to send your friends a challenge the first page you get to when you click the link off the profile is a friend picker. You first choose what friend you want to send the challenge to. Then you set the challenge the word needs to be valid and part of my database I've gathered of 48000 + words. This stops people from using bad words and making up words as that would ruin the game.

![Friend picker](assets/images/pause.PNG)
![Challenge set page](assets/images/pause.PNG)

- __Challenges Page__ 

- This is where you see challenges you've recieved from others.
- This allows users to complete challenges other users have sent them.

![Challenges](assets/images/game-over.PNG)

- __Sent challenges__

- This page allows you to view and edit challenges you've sent to others and see if the person managed to complete the challenge or fail.
- This allows a user to edit the challenge they've sent if they arent happy with the word they sent off origionally it however doesnt allow the word to be edited if the challenge has been started. You may also delete challenges sent aswell.

![Sent challenges](assets/images/highscore.PNG)

- __Freeplay__
  
 - This is a few levels that I have created this allows players to get an idea of what the game is like and wither they like it.

![Freeplay](assets/images/suggestions.PNG)

- __Add friend__
  
- This is where users go to add friends. If youre only just signing in please feel free to add thebrightspark which is my profile and challenge me! 
- Users will be able to add eachother here. It only allows you to add users that exist.

![Add friend](assets/images/colorblind.PNG)

- __Game page__

- This is the main game where users will guess the words and they will display above the inout line in a grid you only have six guesses so mak sure they are good ones! Once you hit the guess limit its game over.
- Users will be able to complete challenges their friends sent them here or complete the freeplay levels.

# Wireframes

### adobe XD

[interactive wireframe](https://xd.adobe.com/view/5fb66345-d813-4c0c-a24d-a927b8edc2d9-0ae5/)

This is the best way other than using the site to get an idea of how everything works

# Challenges overcome 

# Goal

Displaying the correct amount of boxes on the game screen and the guesses to display and change the box background if the letter was in the right spot

# Issue

The correct amount of boxes relies on the html page knowing how many letters are in the word getting that info wasnt straight forward initially as I had no idea how to do it. 

It also relied on the html page knowing that the letter was in the right place and what the correct answer was without displaying it to the user

## How I did it

After looking back at previous mini project: task manager I noticed we used |length to find the length of a word which solved the first problem

next was the conditional formatting of the box it sits in the way I implemented this was by using loop.index0 to check the letters of both the guess and the answer match and then also used the in keyword in jinja to check if the letter was part of the word string. If the letter was in the correct place it adds the class correct if not it moves on to checking if its in the word if it is a letter included in the word it adds the class nearly otherwise it just displays the same color as normal.

## Goal

To get the words onto the database

## Issue

I had a dictionary of 100k plus words varying in length and some even inclding special characters like "-" so the goal was to filter those out and only send over words between 5-8 letters long.

I didnt have time to do this manually

## How I did it

I created an app to iterate over the 100k words filter out any that include "-" and only send over the words if the length is '>' 4 and '<' 9 it took about 30 mins but when it was done I had 48k words and their definitions added to the mongo db database.

## Goal

get the page to display the guesses correctly

## Issue

Upon submit the HTML page refreshes this causes the page to rebuild and send off the info at the same time...
problem here is that the system requests the info down from the server which at this point hasnt recieved the new guess so the new guess isnt displayed... 

I submit the form using javascript and the refreshing of the page means I dont need to clear all the input boxes which is ideal. Saves me creating an extra function and am not aware of a way of sending info from a html page to python without submitting

Also upon manual refreshing it sends the same guess through again which means refreshing the page again after a second delay is not an option

## How I did it

I sent the guess back to the HTML page via python I had to first of all add some if statements to check if any of the guesses had already been guessed then I would create a new dict that included the guess at the correct line. 

There is a small bug left here though if you manage to guess twice in less than 500ms it can cause and issue where the first guess is lost but doing this is very difficult and extremely unlikely.

I also go the python app to check if the guess had already been guessed and blocked it if it had. 
This lead to a lengthy function but it worked so thats all that mattered.

## Goal

## Issue

## How I did it

# Technology used
## wireframes
- adobe XD
## Frameworks
- I used github to store the repository and version management
- I used gitpod for editing the code and for posting to github 
## Libraries
- I used [Jquery]() to make javascript easier to write.
- I used [Emailjs]() to make the suggestion page work.

# user story 

The users will be people just looking to relax and play something simple and fun. No minimum requirements and accessible from all devices too so users will be all kinds of people on all kinds of devices.

### Features Left to Implement

- difficulty settings easy, medium, hard
- lives
- keyboard controls to make it possible for blind people to play (the game reads out the instrustions everytime the command function is called)

## Testing 

### Issues during development 

### big bugs

# Timer bug

## description

- This is a bug that seems to come from the delay. So during the setTimeout function where it waits a second during that second if timer function is called it causes a bug where it stops the new timer to be called and then after the delay the old timer is called leading to the player being unable to continue playing. 
- The bug is gamebreaking and so needs to be resolved.
- In order to fix this issue I first must make the logic aware the timer is waiting. To do this I will create a global variable called wait which is set to true just before the set timeout. in the set timeout it will also toggle it to be false.
- This will allow me to implement a check so that if timeout is waiting it will stop any new timer calls. until the old timer has been stopped.
- This "fix" resulted in a delay to the player and this is unacceptable.
-  New fix idea is to set timeLeft as a global variable and have the timer only decrease it and not carry a value this will result in me being able to set the variable at anypoint and the timer will just decrease it by one and update the timer value.
- Doing this caused a new bug where timer would be called during every answer leading to timer decreasing the timeLeft variable multiple times a second instead of once as it was playing through.
- Resolved the first bug by deleting the timer() calls in other functions so it's not called more than once but now for some reason which I haven't figured out yet the timeLeft is being set at 5 by the correct function but its being updated to 3 then 2 then 1 its like its skipping 5 and 4. will look into this at next opportunity.
- figured out this is due to an error in my correct function I had the numbers the wrong way round instead of it starting easier and getting harder it was starting harder and getting easier. This however doesnt stop the gameovers that happen due to the timer continueing to countdown meaning you only eally hve 4 seconds as if you put an answer in in the last second the script will set the timer to stop but it will only be stopped after it hits 0.
- This time I'm going to try a different approach Im going to create an infinite loop that updates every 10ms each 100ms it will add 1 to a timecounter variable if time counter hits 10 then that means a second has passed and it will call a function to update the timer. 
- This should in theory create a much more responsive timer that will also allow for an easy reset as at anypoint I need to reset the timer it will send it back to 0 so max the timer will be slow or fast is by 99ms each way which I personally deem acceptable.
- Timer was fixed by me quickly revising how to use the setTimeout() function the ,100 needed to be within the bracket and I also needed it to be a variable. 
- Credit goes to : [we3 schools](https://www.w3schools.com/jsref/met_win_settimeout.asp)

### small bugs

# Correct answer fix

## description 

- This is not necessarily a bug but it looks like one sometimes when you click the correct answer it will display the exact same question again which makes it look like the game didnt register the click when it actually does.
- The playtester advised maybe a green light or some indication you got it right.
- will add to the to do list.
- The timer bug also returned upon pressing play again which is something I thought I fixed.
- playtester got score of 885 and wanted it to be in the highscore under name rhi.

# Themes bug/ change

## description 

- changed name to colorblind mode as that all it really does.

# Kera bugstester 

## description 

- I posted the game to the slack community and kera replied saying the form wasnt displaying correctly which I quickly corrected.
- She also posted a highScore which I added to the highscore page

# Niall bugtester

## description

- I then posted it to my facebook page so a few friends could post their scores and let me know of any bugs 
- Niall pointed out that the dont should be don't 

# Playtesters opinions

### Niall

- By the way its don't (score:360)

### Rhi 

- Needs a way of telling if the game registered a correct answer wasnt sure if it was bugged or not sometimes. (score:1021)

### Sharron

- Its actually a good game for cognitive development and verbal reasoning. You have to read and focus. Might be good for people at risk of dementia or brain injury. I read about plasticity and how the brain can rewire itself when damaged. (score: 368)

### Giles 

- Not bad (score: 493)

### Ashley 

- Very addictive game. Hows this for a top score 989 (score: 989)

### Dean 

- Actually really good my girlfriend is addicted to it (score: 737)

### Josh

- Love this Dan! If I hadn't had a few glasses of wine and playing ps2 I would give it a good old go. I'm going to save the link and try again tomorrow (score: 82)

### Rachel 

- poxy game (score: )


### lighthouse Testing 

![Mobile results](assets/images/mobile-lighthouse-report.PNG)
### Two issues 
- First issue is performance as the background image is a jpg I should have saved and uploaded it in a better format it delays loading by 0.75 ms so not a concern really 
- Second is a security vulnerabilities due to me connecting to Jquery this will go unfixed as its not a big risk.
![Desktop results](assets/images/desktop-lighthouse-report.PNG)
### One issue
- Only issue is security vulnerabilities due to me connecting to Jquery this will go unfixed as its not a big risk.

### Validator Testing 

# HTML
 ## index.html
  - No errors were returned when using the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebrightsparkdev.github.io%2FDan-says%2F#textarea)
 ## suggestions.html
  - No errors were returned when using the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebrightsparkdev.github.io%2FDan-says%2F#textarea)
# CSS
 ## style.css
  - No errors were found when using the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fthebrightsparkdev.github.io%2FDan-says%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
# JS
 ## gameLogic.js
 - No errors were found but there are 37 warnings mainly talking about es6 syntax <--(later discovered this is due to me not adding a comment before posting my code) and Jquery syntax[JShint validator](https://jshint.com/)
 ## sendEmail.js
 - no errors were found other than those relating to references to Jquery script


### Unfixed Bugs

 - 37 warnings from JShint 
 - JShint states about the redefinition of name this is a bug that doesnt cause any issues at all as it relates to a sub category of highscores object array (I may fix this as it's quite simple just for the sake of completion)

## Deployment

I was using github as the repository for the whole project so when I wanted to create a live page it was very easy to do.

- The site was deployed to GitHub pages. The steps to deploy are as follows:
  - In the GitHub repository, navigate to the Settings tab
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.
  - Make sure to select root before saving.

- The site was deployed to GitHub pages. 

The live link can be found here - [Dan says](https://thebrightsparkdev.github.io/Dan-says/)


## Credits 

Below are the sources of all the media and content 

### Almost no parts of the code on this website are copy and pasted 

- If I was struggling with anything I would simply go to website that I have linked below and read up on how to use the specific code and then I would simply use the code correctly. 
- all websites used are linked below:
- [google fonts](https://fonts.google.com/)
- Code Institute mentor also sent me a link to a template of a README.md to create a structure I changed everything and kept structure apart from the steps to deploy as there isn't anything to change added a bit about making sure it was root as docs brings up an error message for me saying failed to build.
- [Helped create the timer](https://dev.to/gspteck/create-a-stopwatch-in-javascript-2mak)
- [how I learned about remove Event listener](https://stackoverflow.com/questions/4402287/javascript-remove-event-listener)
- [Helped me learn how to toggle classes](https://www.w3schools.com/howto/howto_js_toggle_class.asp).
- [copy pasted this code](https://stackoverflow.com/questions/8057802/html-button-close-window)

### Content 



### Media

### JavaScript help
- [Helped create the timer](https://dev.to/gspteck/create-a-stopwatch-in-javascript-2mak)
- [how I learned about remove Event listener](https://stackoverflow.com/questions/4402287/javascript-remove-event-listener)
 # More coming soon! 
 
 ### Follow me on github to stay upto date and message me for project ideas/pitches always ready to work with someone.
 
 # devDiary
 # 11/01/2022
 ## things that need fixing/ implementing from this point onwards:
 ### The timer needs to reset without calling checkAnswer 
 #### how I did it - 12/01/2022 - 
 ##### fixed the issue quickly: 
  - Added a var with global scope. 
  - Added a check in the timer to see if stop is toggled to true.
  - If stop = true then the timer stops and sets stop to false.
  - Added a toggler in the checkAnswer function to toggle stop to true so whenever a button is pressed it checks the answer is correct calls a function either gameOver or correct and then stops the timer.
 ### The timer needs to be able to be stopped 
 #### how I did it 12/01/2022
 ##### very simple
 - fixed by correcting the timer (above)
 ### The pause function will be tricky to implement if timer is unstoppable 
 #### how I did it 12/01/2022
 ##### very simple
 - fixed by correcting the timer (above)
 ### make the text display in the correct location
 #### how I did it - 14/01/2022 - 
 ##### I asked my mentor and he gave me a few hints
 - The text was hard to move around because it was within a div that was transformed 45deg.
 - we had to remove it from the div and create a new div to hold the text.
 - then we would use position absolute and relative to get the text to display in the correct locations
 - the same was done with the highscore and the play again button
 ### add a call to command in the correct function 
 #### how I did it - 13/01/2022 - 
 ##### very simple 
 - added a command to the correct function
 ### The gameOver screen needs to be created 
 #### how I did it - 14/01/2022 -
 ##### very simple 
 - added to the gameOver function the entire HTML of the page and just edited the bits that needed editing (which was most of it).
 ### The scoring system needs to be implemented
 #### how I did it 14/01/2022 -
 ##### simple
 - added a global var called score and added a bit of code to the correct function to call a score incrementer function.
 ### The colorblind theme needs to be implemented
 #### how I did it - 14/01/2022 -
 ##### simple
 - added text and displayed it still need to add the function to toggle it off/on.
 ### The play Again button needs to be implemented
 #### how I did it 14/01/2022
 ##### tricky
 - I had to add the entire body of the game to the function so that it updates it. tried not adding parts that weren't relevant ended up not displaying correctly so had to just add it all.
 - I also had to add many event listeners that I had removed in the gameover function and remove the ones I had added during the gameover function
 - Finally I had to restart the timer().
 # 14/01/2022
 - tasks added
 ### need to correct the issues in my css code
 #### how I did it 14/01/2022
 ##### very simple
 - issues where empty tags deleted empty tags
 ### implement the gameover messages
 #### how I did it 14/01/2022
 ##### tricky
 - added an array with all possible messages and created a very long if statement to call the correct one depending on current score.
 ### default the theme to standard
 #### how I did it 
 - I added the class standard to all elements that needed to be changed.
 - changed name of themes to colorblind mode as thats all it toggles.
 ### implement themes button
 #### how I did it
  - added an event listener that calls a function that toggles a colorblind class on/off 
  - used [w3schools](https://www.w3schools.com/howto/howto_js_toggle_class.asp) to help me learn how to do this.
 ### fix timer bug 
 #### how I did it 
  - More details are found above in the bug fix section as it was a major problem for me.
  - Short answer is I used setTimout to increment a number the timer displays seconds left each time the timer increments by 10 the seconds reduces by 1 this allows me to have a responsive timer.
 ### The quit button needs to be implemented
 #### how I did it 24/01/2022
   - used an article that explains how to implement a quit function [code used](https://stackoverflow.com/questions/8057802/html-button-close-window).
 ### Implement the pause feature
 #### how I did it 24/01/2022
  - the pause function was tough to implement because I was looking to darken the foreground infront of the main game and add text saying Unpause to indicate pressing the game section will unpause. I will look towards the best way to implement it soon. otherwise the pause function so far is functional but unpausing is not yet possible. 
 ### Implement the unpause fuction
 #### how I did it 24/01/2022
  - the Unpause feature involved changing the pause feature instead of replacing the entire page which would lose the current colorblind setting and set it to default (which was an issue) instead I decided to create a hidden element that is set to visible whenever the game is paused. When it is clicked it then makes itself invisible again and continues the timer. 
  - Works perfectly so far will ask bug testers to try it out extensively. 
 ### implement suggestions
 #### how I did it 25/01/2022
  - Created a new page called suggestions.html and created a form in the dan says theme.
  - Yet to implement EmailJS.
 ### green indicator when right 
 #### how I did it 25/01/2022
  - Created a div thats green with 50% opacity and toggled it on then off for .1 of a second to indicate a correct answer.
 ### The highscores need to be implemented
 #### how I did it 26/01/2022
  - Created some styles in Style.css to style the highscore.
  - Created some javascript functions to create the highscore table and to remove the highscore and call gameover.
  - Got a few people to play the game to get some hgihscores to put on the board.
 ### Implement EmailJS
 #### how I did it
  - After a quick read through the documentation for EmailJS it was quite straight forward to implement.
 ### implement tutorial
 #### how I did it 28/01/2022
  - first created a function to start the tutorial and an event listener to call it
  - then created a function that increments the rounds and resets when limit is reached it also creates an event listener to move onto the next round on the correct answer
  - created a highlighter function that is meant to display only the correct answer and hide the rest using classtoggle this is called by the tutorial round function 
  - the tutorial round function also calls a command to display at the top of the page just like in game but the command is set to certain messages
  - then there the tips function that displays a message in the blank spaces to tell the user why that answer is the correct answer.
  - when the tutorial is over I origionally planned for it to refresh the page but due to it creating a dialog box saying are you sure you want to refresh i decided upon setting the html to its origional state allowing me to also keep the colorblind setting intact.
  - I could of hidden the colorblind tags but decided not to as it doesnt benefit anyone.

  to do 
  make sure sign in and sign up pages have a way of going back to the meain menu