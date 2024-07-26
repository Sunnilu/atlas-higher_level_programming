#!/usr/bin/node
const fs = require('fs'); // Corrected the import statement
const file = process.argv[2]; // Assuming the second argument is the file path
const content = process.argv[3]; // Assuming the third argument is the content to write

// Explicitly casting content to a string just in case
const contentString = typeof content === 'string' ? content : String(content);

fs.writeFile(file, contentString, 'utf-8', function (err) { // Corrected the function name and usage
    if (err) {
        console.log(err);
    } else {
        console.log("File written successfully.");
    }
});


