// declaring global variables
let letters = []
let keyBoardItems = document.getElementsByClassName("keyboard-square")
// puts the letter in the correct box
function typeLetter(content){
    console.log(content)
}
// determines what was clicked and if it's valid
function keyboardClick(letter){
    console.log(letter)
    typeLetter(letter)    
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

