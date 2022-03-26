// declaring global variables
let letters = [];
let currentInputBox = "1";
let inputBoxes = [];
let length = document.getElementById("length").getAttribute("length");
let correct = document.getElementsByClassName("complete")
let currentWord = [];
let currentGuess = [];
let keyBoardItems = document.getElementsByClassName("keyboard-square");
let inputSquares = document.getElementsByClassName("input-square");
console.log(correct)
for (element in correct){
    console.log(element)
    if (element < 6){
    let attribute = correct[element].getAttribute("complete")
    if (attribute == "yes"){
        currentInputBox = "completed"
    }}
}
// submits and checks answer
function submitAnswer(){
    document.getElementById("answer").value = currentWord
    document.getElementById("submit").submit()
}
// deletes a letter and decreases the value of current input box by 1
function backspace(){
    if(currentInputBox > 1){
        parseInt(currentInputBox)
        currentInputBox--
        toString(currentInputBox)
        let box = document.getElementById(currentInputBox)
        box.children[0].innerText=""
        currentWord = currentWord.slice(0,-1)
        console.log(currentWord)
    }
}
// puts the letter in the correct box
function typeLetter(content){
    // increments the current input box
    if (currentInputBox < length){
        let box = document.getElementById(currentInputBox)
        box.children[0].innerText=content
        parseInt(currentInputBox)
        currentInputBox++ 
        toString(currentInputBox)
        console.log(currentWord)
    }
    else {
        let box = document.getElementById(currentInputBox)
        box.children[0].innerText=content
        parseInt(currentInputBox)
        currentInputBox = 0
        toString(currentInputBox)
        submitAnswer()
        console.log(currentWord)
    }   
}
// determines what was clicked and if it's valid
function clicked(letter){
    if (letter == "Backspace"){
        backspace()
    }
    letter = letter.toLowerCase()
    if (letters.includes(letter)){
        currentWord += letter
        typeLetter(letter)
    }   
}
// translates the keyboard click events into correct format for clicked function above
function keyboardClick(event){
    let letter = event.key
    clicked(letter)
}

// creates a string that includes available letters
for (let item in keyBoardItems){
    let letterHolder = keyBoardItems[item]
    if (letterHolder.innerText != undefined){
        let letter = letterHolder.innerText
        letters += letter
    }
}
// creates event listener for keyboard presses and calls the keyboardClick function
document.addEventListener("keydown", function(){keyboardClick(event)})
