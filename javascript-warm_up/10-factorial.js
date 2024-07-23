#!/usr/bin/node
// define a recursive function to compute factorial.
let args = parseInt(process.argv[2]);
if (isNaN(args)) {
  args = 1;
}
function factorial (n) {
  if (n == 1) {
    return 1;
  }
  // recursive case: n * factorial
  return n * factorial(n - 1);
}
console.log(factorial(args));
