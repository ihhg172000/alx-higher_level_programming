#!/usr/bin/node
import { argv } from 'node:process';

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  const numbers = argv.slice(2);

  numbers.sort((a, b) => {
    return a === b ? 0 : (a > b ? -1 : 1);
  });

  console.log(numbers[1]);
}
