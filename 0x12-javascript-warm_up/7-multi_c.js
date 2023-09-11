#!/usr/bin/node
import 'node:process';

const occurrences = parseInt(process.argv[2]);

if (!occurrences) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < occurrences; i++) {
  console.log('C is fun');
}
