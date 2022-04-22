/**
 * @jest-environment jsdom
 */

// in order to test the script please go into the javascript and comment out the let length i've made it clear on the file itself also

const { currentInputBox, correct, typeLetter, clicked, letters, keyBoardItems, currentWord}= require("../script");



describe("Tests if the functions that depend on the HTML function correctly", () => {
    beforeAll(() => {
        let fs = require("fs");
        document.open();
        document.write(`<html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Word VS</title><link rel="stylesheet" href="/static/css/style.css" type="text/css"></head><body><main class="game-body"><div class="hidden-off-screen-container"><form method="POST" id="submit" class="hidden-off-screen-element" action="/game/62544bae7b50e428ab8755b8"><label for="answer">answer</label><input id="answer" type="text" name="answer" class="validate" value="" required=""></form></div><div class="game-area"><div class="responsive-large margin-bottom"><h6>rhiharries's challenge</h6><div class="rounded responsive-small"><a href="/challenges"><h6>back</h6></a></div></div><div class="rounded guess-box margin-bottom" id="length" length="6"><div class="game-line complete" complete="no"><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div></div><div class="game-line complete" complete="no"><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div></div><div class="game-line complete" complete="no"><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div></div><div class="game-line complete" complete="no"><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square">
        <h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div></div><div class="game-line complete" complete="no"><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div></div><div class="game-line complete" complete="no"><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div><div class="game-square"><h3></h3></div></div></div><div class="game-line margin-bottom"><div class="input-square" id="1"><h3></h3></div><div class="input-square" id="2"><h3></h3></div><div class="input-square" id="3"><h3></h3></div><div class="input-square" id="4"><h3></h3></div><div class="input-square" id="5"><h3></h3></div><div class="input-square" id="6"><h3></h3></div><img id="backspace" letter="Backspace" onclick="clicked(this.getAttribute('letter'))"src="/static/images/backspace.png"></div><div class="rounded keyboard-bg"><div class="keyboard-square" letter="s" onclick="clicked(this.getAttribute('letter'))"><h3>s</h3></div><div class="keyboard-square" letter="e" onclick="clicked(this.getAttribute('letter'))"><h3>e</h3></div><div class="keyboard-square" letter="w" onclick="clicked(this.getAttribute('letter'))"><h3>w</h3></div><div class="keyboard-square" letter="y" onclick="clicked(this.getAttribute('letter'))"><h3>y</h3></div><div class="keyboard-square" letter="n" onclick="clicked(this.getAttribute('letter'))"><h3>n</h3></div><div class="keyboard-square" letter="h" onclick="clicked(this.getAttribute('letter'))"><h3>h</h3></div><div class="keyboard-square" letter="u" onclick="clicked(this.getAttribute('letter'))"><h3>u</h3></div><div class="keyboard-square" letter="l" onclick="clicked(this.getAttribute('letter'))"><h3>l</h3></div><div class="keyboard-square" letter="f" onclick="clicked(this.getAttribute('letter'))"><h3>f</h3></div><div class="keyboard-square" letter="a" onclick="clicked(this.getAttribute('letter'))"><h3>a</h3></div><div class="keyboard-square" letter="t" onclick="clicked(this.getAttribute('letter'))"><h3>t</h3></div></div><!-- scripts --><script type="text/javascript" src="/static/js/script.js"></script></div></main></body></html>`
        );
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
        clicked("a")
        clicked("z")
        clicked("y")
        clicked("t")
        expect(currentWord).toBe("at")
    })
})