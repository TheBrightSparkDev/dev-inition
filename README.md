`python3 -m http.server`
# [Dan says](https://thebrightsparkdev.github.io/Dan-says/)

Link to site [Dan says](https://thebrightsparkdev.github.io/Dan-says/)

Dan Says is a fun Simon says game with a comedic twist I tried to add as much of my own personality and humour into this game in order to help people feel
connected to the developer this game stands as an example that sometimes even a simple concept can be made fun by more than just the gameplay but with funny
quips and messages. It also incorporates a contact page where people can let me know how to improve the game and let me know of any bugs. I created the game so it can be used on multiple devices.

<img src="assets/images/responsive-readme.png" alt= "image of the website on various devices to show responsiveness" width="100%">

desktop and background credit: [pixabay](https://pixabay.com/photos/apple-computer-desk-workspace-1868496/)

## Features 

### The first menu

- __Main menu__

  - The main menu contains a few options for the user to change the theme (colorblind), make suggestions and access the tutorial.
  - These are to make the user feel more comfortable, make the game better and be involved and finally to show the user how to play the game.

![Main menu](assets/images/main-menu.PNG)

- __Game screen__

  -  This is where users will be most of the time unless they dont do so well... It's the main game! 
  -  Users will hopefully find this fun and repeatable and will hopefully look forward to seeing the funny messages that pop up at the end as they vary depending on how well you do.

![Game screen](assets/images/game-screen.PNG)

- __Tutorial__

  - This is where users will be able to learn to play the game it works by darkening the background and highlighting the correct answer and explaining why it's the right answer.
  - I wanted this to be short and sweet so that users don't get bored before actually playing the game I spent alot of time making sure I could explain the game in as little time as I could. 

![Tutorial](assets/images/tutorial.PNG)

- __Pause menu__

  - I wanted this to be very easy to access so made it so that the user can activate the pause menu by clicking the message above the gamezone.
  - This allows users to either change themes (colorblind) during the game or quit or just take a break if they are on a highscore they don't want to lose.

![Pause menu](assets/images/pause.PNG)

- __Game over!__ 

  - This is the page you see whenever you lose it includes options for users to look at other highscores set by either myself during development or fictional characters or play again also shows the score they obtained during the last playthrough it also includes a funny message to say how well or not so well the user has done. 
  - This will hopefully drive the user to want to do better and beat the fictional characters or just play again whatever motivates them!.

![Game Over](assets/images/game-over.PNG)

- __Highscores__

  - This is a self explanatory section really just shows the highscores and shows the users score on the board if they did well enough to make it up there.
  - This is to motivate users to push to beat the playtesters. 

![Highscores](assets/images/highscore.PNG)

- __Suggestions__
  
  - This is a form where users can add their thoughts about the game and let me know what they would change or tell me about any bugs that I may have missed. It also allows me to reply to them and interact with them afterwards if they leave their email.
  - This is in my opinion essential for every game as sometimes the developer doesn't realise the real reason their game is used. 

![Suggestions](assets/images/suggestions.PNG)

- __ColorBlind Mode__
  
  - This is for users that are colorblind it basically adds text to the different options so that users who are colorblind know whats what.
  - This is my way of making sure the game is accessible to as many users as possible. 

![ColorBlind Mode](assets/images/colorblind.PNG)

# Wireframes

### adobe XD

[interactive wireframe](https://xd.adobe.com/view/5fb66345-d813-4c0c-a24d-a927b8edc2d9-0ae5/)

This is the best way to get a good idea of how the game plays and was the first thing I made when designing the webpage.

## Javaplanning

### images of JavaPlanning! 

I started on a piece of paper when I first thought of what idea I would like to go with

![Initial sketches](assets/images/javaplanning-sketch-1.jpg)

I then continued in my code planning book which allowed to sketch next to the actual code in a more ordered fashion.

![Code book sketches](assets/images/javaplanning-sketch-2.jpg)
![Code book sketches](assets/images/javaplanning-sketch-3.jpg)
![Code book sketches](assets/images/javaplanning-sketch-4.jpg)

I wasnt lying! I really did write java code on paper... 

# challenges overcome 
- timer(){} this was a tough one to figure out and googling didnt help much since most places said about Thread.sleep which was throwing an error at me! I did find a site where someone had created a stopwatch and spotted they used timeout to call the function again and this is what inspired me to try it myself as origionally it was a for loop which was running through instantly nomatter what I did.
- I needed to change what the middle button does when clicked so had to remove the eventListener to start the game.
- One of the play testers said that sometimes the game would give the same question twice and that it felt like it was a bug as if she hadnt clicked anything due to there being no feedback so created a div that is is green with a high opacity and toggled an invisible class on and off for 0.1 seconds everytime a correct answer is pressed.
- Suggestions not diplaying correctly this was picked up by another playtester on a mobile I fixed the issue by changing the widths of the boxes to 100%.
- more details on each of these challenges are found below in the bug section
- Anti cheat mecnanism the way I was making sure the scores were correct is by double checking the message to see if it lined up with the screenshot of their highscore if the message didnt add up the score wasnt added.

# Technology used
## wireframes
- adobe XD
- good old pen and paper
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