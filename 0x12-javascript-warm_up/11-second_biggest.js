#!/usr/bin/node
import { argv } from 'node:process';

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  const numbers = argv.slice(2).map(value => {
    return +value;
  }).sort((a, b) => b - a);

  console.log(numbers[1]);
}
