#!/usr/bin/node
// a function that returns the number of occurrences in a list.
exports.nbOcurrences = function (list, searchElement) {
    return list.reduce((a, v) => (v === searchElement ? a + 1 : a), 0);
};