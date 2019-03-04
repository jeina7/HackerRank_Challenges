// Hackerrank 10 Days of JavaScript
// https://www.hackerrank.com/domains/tutorials/10-days-of-javascript
// Day 2

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

function getLetter(s) {
    let letter;
    let result;
    var arrs = ['aeiou', 'bcdfg', 'hjklm', 'npqrstvwxyz'];

    for (var i = 0; i < arrs.length; i++) {
        if (arrs[i].includes(s[0])) {
            result = i
        }
    }

    switch (result) {
        case 0:
            letter = "A"; break;
        case 1:
            letter = "B"; break;
        case 2:
            letter = "C"; break;
        case 3:
            letter = "D"; break;
    }

    return letter;

}


function main() {
    const s = readLine();

    console.log(getLetter(s));
}
