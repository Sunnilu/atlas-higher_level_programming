#!/usr/bin/node
// prints the first argument passed to it.

const args = process.argv.slice(2);
// checking if there are any arguments passed
if (args[0] !== undefined) {
    console.log(args[0]);
} else {
    console.log("No argument");
}