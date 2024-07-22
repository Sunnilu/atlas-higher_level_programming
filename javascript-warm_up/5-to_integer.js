#!/usr/bin/node
// Prints My Number if the first argument is successfully coverted to integer.
const args = process.argv.slice(2);
// trying to convert the first argument to an integer
const num = Number(args[0]);
// see if the conversion is successful
if (!isNaN(num)) {
    console.log ('My number: ${89}');
} else {
    console.log('Not a number');
}