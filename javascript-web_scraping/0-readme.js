#!/usr/bin/node
// a script that reads and prints the contents of a file
const fs = require('fs');

// Check if a file path is provided
if (process.argv.length < 3) {
  console.log('Usage: node script.js <file_path>');
  process.exit(1); // Exit the script if no file path is provided
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(`An error occurred: ${err}`);
    return;
  }
  console.log(data);
});
