#!/usr/bin/node
// prints a message depending arguments passed.
const args = process.argv.slice(2);

if (args.length === 0) {
    console.log("No argument");
} else if (argrs.length === 1) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}