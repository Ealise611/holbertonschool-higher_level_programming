#!/usr/bin/node

function fact (n) {
  let res = 1;
  for (let i = 1; i <= n; i++) {
    res *= i;
  }
  return res;
}
const n = process.argv[2];
console.log(fact(n));
