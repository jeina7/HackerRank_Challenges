// Hackerrank 10 Days of JavaScript
// https://www.hackerrank.com/domains/tutorials/10-days-of-javascript
// Day 4

class Polygon {
    constructor(lengths) {
        this.lengths = lengths;
    }

    perimeter() {
        var sum = 0;
        for (var i = 0; i < this.lengths.length; i++) {
            sum += this.lengths[i];
        }
        return sum;
    }
}



const rectangle = new Polygon([10, 20, 10, 20]);
const square = new Polygon([10, 10, 10, 10]);
const pentagon = new Polygon([10, 20, 30, 40, 43]);

console.log(rectangle.perimeter());
console.log(square.perimeter());
console.log(pentagon.perimeter());
