#!/usr/bin/node

const request = require('request');

// URL from command line argument
const url = process.argv[2];

request(url, function (error, response, body) {
    if (error) {
        console.error('Request failed:', error);
        return;
    }

    try {
        // Parse the body of the response
        const data = JSON.parse(body);
        const results = data.results;

        // Count the number of movies featuring character ID 18
        const count = results.reduce((acc, movie) => {
            return movie.characters.some(character => character.endsWith('/18/'))
                ? acc + 1
                : acc;
        }, 0);

        // Output the result
        console.log(count);

    } catch (e) {
        console.error('Failed to parse response:', e);
    }
});
