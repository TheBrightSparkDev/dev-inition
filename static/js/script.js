// declaring global variables
let letters = []
let keyBoardItems = document.getElementsByClassName("keyboard-square")
let inputSquares = document.getElementsByClassName("input-square")
// puts the letter in the correct box
function typeLetter(content){
    console.log(content)
}
// determines what was clicked and if it's valid
function clicked(letter){
    if (letters.includes(letter)){
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
