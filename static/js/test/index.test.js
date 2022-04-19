/**
 * @jest-environment jsdom
 */

const {length}= require("../index");


describe("Tests if the functions that depend on the HTML function correctly", () => {
    beforeAll(() => {
        let fs = require("fs");
        let fileContents = fs.readFileSync("index.html", "utf-8");
        document.open();
        document.write(fileContents);
        document.close();
    });
    test("Checks if HTML is loaded", () => {
        expect(length).toBe(6)
    })
})