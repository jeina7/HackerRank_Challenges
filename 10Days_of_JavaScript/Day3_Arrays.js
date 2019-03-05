// Hackerrank 10 Days of JavaScript
// https://www.hackerrank.com/domains/tutorials/10-days-of-javascript
// Day 3

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

function getSecondLargest(nums) {
    var Number = Math.max.apply(null, nums);
    while (nums.length > 0) {
        nums.splice(nums.indexOf(Number), 1);
        if (nums.indexOf(Number) == -1) {
            break;
        }
    }
    Number = Math.max.apply(null, nums);
    return Number;
}


function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);

    console.log(getSecondLargest(nums));
}
