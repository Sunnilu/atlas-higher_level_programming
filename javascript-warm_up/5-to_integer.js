#!/usr/bin/node
// Prints My Number if the first argument is successfully converted to integer.
const args = process.argv[2]; // corrected the syntax for accessing command line arguments

// trying to convert the first argument to an integer
if (args === undefined || isNaN(parseInt(args))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(args)}`); // added a space after the colon for better formatting
}
