#!/usr/bin/node
// script that prints two arguments passed to it.

const args = process.argv.slice(2);

// checking if at least two arguments are passed
if (args.length >= 2) {
    console.log('${args[0]} is ${args[1]}');
} else {
    console.log("Not enough arguments provided.");
}