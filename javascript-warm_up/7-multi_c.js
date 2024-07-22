#!/usr/bin/node
// prints x times C is fun.
const x = process.argv[2];

if (x === undefined || isNaN(parseInt(x))) {
    console.log('Missing number of occurrences');
 } else {
    for (let i = 0; i < parseInt(x); i++) {
        console.log('C is fun');
    }
 }