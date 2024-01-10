#!/usr/bin/node


function add(a, b) {
  console.log(parseInt(a) + parseInt(b));
}

const args = process.argv.slice(2);
add(...args);
