#!/usr/bin/node

const numarg = parseInt(process.argv[2]);

if (!Number.isInteger(numarg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numarg; i++) {
    let row = '';
    for (let j = 0; j < numarg; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
