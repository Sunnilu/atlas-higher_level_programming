#!/usr/bin/node
//prints three specific lines using an array of strings and a loop.
const messages = [
    "C is fun",
    "Python is cool",
    "JavaScript is amazing",
];
// variable to accumulate the final output
let output = '';

for (const message of messages) {
    output += '${message}\n';
}
console.log(output.trim());