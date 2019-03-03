// Hackerrank 10 Days of JavaScript
// https://www.hackerrank.com/domains/tutorials/10-days-of-javascript
// Day 1

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}
/*
 * Create the function factorial here
 */

function factorial(n) {
    if (n == 1) {
        return 1;
    }
    else {
        return n * factorial(n - 1);
    }
}
