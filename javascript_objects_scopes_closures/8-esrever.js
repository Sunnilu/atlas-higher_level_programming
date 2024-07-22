#!/usr/bin/node
// a function that returns the reversed version of a list.
exports.reverse = function (list) {
    // Ensure list is treated as an array and lengths are compared as strings
    const arrList = Array.isArray(list) ? list : [];
    let start = 0;
    let end = arrList.length - 1;

    while (start < end) {
        // Swap elements
        const temp = arrList[start];
        arrList[start] = arrList[end];
        arrList[end] = temp;

        // Move towards the center
        start++;
        end--;
    }

    return arrList;
};
 