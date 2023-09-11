#!/usr/bin/node
import 'node:process';

const number = parseInt(process.argv[2]);

console.log(number || 'Not a Number');
