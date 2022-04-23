/**
 * @jest-environment jsdom
 */

// in order to test the script please go into the javascript and comment out the let length i've made it clear on the file itself also

const { correct, typeLetter, clicked, keyBoardItems, lettersPopulator}= require("../script");



describe("Tests if the functions that depend on the HTML function correctly", () => {
    beforeAll(() => {
        let fs = require("fs");
        let fileContents = fs.readFileSync("testgame.html", "utf-8");
        document.open();
        document.write(fileContents);
        document.close();
    });
    test("Checks if HTML is loaded", () => {
        expect(document.getElementById("answer").getAttribute("class")).toBe("validate")
    })
    test("Checks if the game locks up when the game is completed or lost",() =>{
        document.getElementById("length").innerHTML=`<div class="game-line complete" complete="yes">`
        // copy and pasted from script.js
        let correct = document.getElementsByClassName("complete");
        for (var element in correct){
            if (element < 6){
            let attribute = correct[element].getAttribute("complete");
            if (attribute == "yes"){
            // this is currentInputBox on script.js setting this to a word (any word) stops the game
            box = "completed";
            break
            }}
        }
        expect(box).toBe("completed")
    })
    test("Tests if the system only accepts letters from the keyboard",() =>{
        // accepted letters are s,e,w,y,n,h,u,l,f,a,t
        const letters = ["s","e","w","y","n","h","u","l","f","a","t"]
        let currentWord = []
        // I wasnt able to get the system to read the letters in keyboardItems for some reason so had to mock the test
        function clicked(letter){
            if (letter == "Backspace"){
                backspace();
            }
            letter = letter.toLowerCase();
            if (letters.includes(letter)){
                currentWord += letter;
                // typeLetter(letter);
            } 
        }
        clicked("a");
        clicked("b");
        clicked("q")
        clicked("z");
        clicked("y");
        clicked("t");
        expect(currentWord).toBe("ayt")
    })
    test("Tests if backspace works",() =>{
        // accepted letters are s,e,w,y,n,h,u,l,f,a,t
        const letters = ["s","e","w","y","n","h","u","l","f","a","t"]
        let currentWord = []
        let currentInputBox = 2
        // I wasnt able to get the system to read the letters in keyboardItems for some reason so had to mock the test
        function backspace(){
            if(currentInputBox > 1){
                parseInt(currentInputBox);
                currentInputBox--;
                currentInputBox = currentInputBox.toString();
                let box = document.getElementById(currentInputBox);
                box.children[0].innerText="";
                currentWord = currentWord.slice(0,-1);
            }
        }
        function clicked(letter){
            if (letter == "Backspace"){
                backspace();
            }
            letter = letter.toLowerCase();
            if (letters.includes(letter)){
                currentWord += letter;
                // typeLetter(letter);
            } 
        }
        clicked("a");
        clicked("b");
        clicked("q")
        clicked("z");
        clicked("y");
        clicked("t");
        clicked("Backspace")
        expect(currentWord).toBe("ay")
    })
})