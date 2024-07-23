#!/usr/bin/node

// Function to count occurrences of an element in a list
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    // Convert both list[i] and searchElement to string for strict comparison
    if (String(list[i]) === String(searchElement)) {
      count++;
    }
  }
  return count;
};
