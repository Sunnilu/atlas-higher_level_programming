#!/usr/bin/node
// define the add function.
function add(a, b) {
    return a + b;
}
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.agrv[3]);

if (!Number.isNaN(arg1) && !Number.isNaN(arg2)) {
    const result = add(arg1, arg2);
    console.log(result);
} else {
    // print NaN if either argument is not a valid number
    console.log("NaN");
}