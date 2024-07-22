#!/usr/bin/node
// prints x times C is fun.
const arg = process.argv[2];
const x = parseInt(arg);

if (!Number.isNaN(x) && x > 0) {
    for (let i = 0; i < x; i++) {
        console.log("C is fun");
    }
}   else {
    // Print "Missing number of occurrences" if x is not valid
    console.log("Missing number of occurrences");
}