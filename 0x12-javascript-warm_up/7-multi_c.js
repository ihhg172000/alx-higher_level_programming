#!/usr/bin/node
import { argv } from 'node:process';

const occurrences = parseInt(argv[2]);

if (!occurrences) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < occurrences; i++) {
  console.log('C is fun');
}
