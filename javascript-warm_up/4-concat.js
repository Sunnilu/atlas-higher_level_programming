#!/usr/bin/node
// script that prints two arguments passed to it.

const args = process.argv.slice(2);

// checking if at least two arguments are passed
const arg1 = args[0] || 'undefined';
const arg2 = args[1] || 'undefined';

console.log('${arg1} is ${arg2}');