#!/usr/bin/node

const arg = process.argv.slice(2);

if (arg.length < 2) {
  console.log(0);
} else {
  // convert all array into integer
  const numbers = arg.map(arg => parseInt(arg));
  // remove duplicate and sort
  const sortedarg = [...new Set(numbers)].sort((a, b) => b - a);
  if (sortedarg.length < 2) {
    console.log(0);
  } else {
    console.log(sortedarg[1]);
  }
}
