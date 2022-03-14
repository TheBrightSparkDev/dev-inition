// declaring global variables
let letters = [];
let currentInputBox = "1";
let inputBoxes = [];
let length = document.getElementById("length").getAttribute("length");
let currentWord = [];
let currentGuess = [];
let keyBoardItems = document.getElementsByClassName("keyboard-square");
let inputSquares = document.getElementsByClassName("input-square");
// submits and checks answer
function refresh(){
    
}
timeout = setTimeout(refresh,1000);
function submitAnswer(){

    document.getElementById("answer").value = currentWord
    document.getElementById("submit").submit()
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
        console.log(currentInputBox)
    } else if (currentInputBox == length){
        let box = document.getElementById(currentInputBox)
        box.children[0].innerText=content
        parseInt(currentInputBox)
        currentInputBox = 0
        toString(currentInputBox)
        console.log(currentInputBox)
        submitAnswer()
    }   
}
// determines what was clicked and if it's valid
function clicked(letter){
    letter = letter.toLowerCase()
    if (letters.includes(letter)){
        currentWord += letter
        typeLetter(letter)
    }   
}
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
