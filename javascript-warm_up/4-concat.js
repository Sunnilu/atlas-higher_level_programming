#!/usr/bin/node
// script that prints two arguments passed to it.

const [, , arg1 = 'undefined', arg2 = 'undefined'] = process.argv;
// checking if at least two arguments are passed
console.log('${arg1} is ${arg2}');