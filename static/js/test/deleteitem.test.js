/**
 * @jest-environment jsdom
 */

// in order to test the script please go into the javascript and comment out the let length i've made it clear on the file itself also

const check = require("../deleteitem");



describe("Tests if the functions that depend on the HTML function correctly", () => {
    beforeAll(() => {
        let fs = require("fs");
        let fileContents = fs.readFileSync("deleteitemtest.html", "utf-8");
        document.open();
        document.write(fileContents);
        document.close();
    });
    test("Checks if HTML loaded correctly",() =>{
        expect(document.getElementById("challenge").innerHTML).toBe("")
    })
    test("Checks if the class tag hide is added",() =>{
        check("challenge");
        expect(document.getElementById("challenge").classList).toContain("hide")
    })
})
