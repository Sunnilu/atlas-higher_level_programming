#!/usr/bin/node
// Prints My Number if the first argument is successfully coverted to integer.
const args = process.argv.[2]
// trying to convert the first argument to an integer
if (arg === undefined || isNaN(parseInt(args))) {
    console.log ('Not a number');
} else {
    console.log(`My number:${parseInt(args)}`);
}