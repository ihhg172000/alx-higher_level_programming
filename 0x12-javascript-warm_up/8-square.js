#!/usr/bin/node
import 'node:process';

const size = parseInt(process.argv[2]);

if (!size) {
  console.log('Missing size');
}

let i = 0;

while (i < size) {
  console.log('X'.repeat(size));
  i++;
}
