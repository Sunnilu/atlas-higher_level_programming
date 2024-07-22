#!/usr/bin/node
// Prints a square of X characters based on size from first argument.
const arg = process.argv[2];
const size = parseInt(arg);

// check if size is a valid number and greater than zero.
if (!Number.isNaN(size) && size > 0) {
    // loop through each row to print the square
    for (let i = 0; i < size; i++) {
        const row = "X".repeat(size);
        console.log(row);
    }
} else {
    console.log("Missing size");
}