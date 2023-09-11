#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2).map(value => {
    return +value;
  }).sort((a, b) => b - a);

  console.log(numbers[1]);
}
