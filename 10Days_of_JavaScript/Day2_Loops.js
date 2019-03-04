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

function vowelsAndConsonants(s) {
    var vowels = 'aeiou';
    let vowel_result = '';
    let consonants_result = '';

    for (var i = 0; i < s.length; i++) {
        if (vowels.includes(s[i])) {
            vowel_result += s[i];
        } else {
            consonants_result += s[i];
        }
    }

    var result = vowel_result + consonants_result;

    for (var i = 0; i < result.length; i++) {
        console.log(result[i]);
    }
}


function main() {
    const s = readLine();

    vowelsAndConsonants(s);
}
