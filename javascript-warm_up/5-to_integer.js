#!/usr/bin/node

const numarg = parseInt(process.argv[2]);

if (Number.isInteger(numarg)) {
  console.log(`My number: ${numarg}`);
} else {
  console.log('Not a number');
}
