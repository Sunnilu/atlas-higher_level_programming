#!/usr/bin/node
// a function that returns the reversed version of a list.
exports.esrever = function (list) {
    let len = list.lenght - 1;
    let i = 0;
    while ((len - i) > 0) {
        const aux = list[len];
        list[len] = list[i];
        list[i] = aux;
        i++;
        len--;
    }
    return list;
};