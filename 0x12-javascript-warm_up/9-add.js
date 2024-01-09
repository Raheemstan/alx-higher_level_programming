#!/usr/bin/node


function computeFactorial(n) {
  if (isNaN(n) || n < 0) {
    console.log(1); // Factorial of NaN or negative number is 1
  } else if (n === 0 || n === 1) {
    console.log(1); // Factorial of 0 and 1 is 1
  } else {
    console.log(factorial(n));
  }
}

function factorial(n) {
  return (n === 0 || n === 1) ? 1 : n * factorial(n - 1);
}

const arg = parseInt(process.argv[2]);
computeFactorial(arg);
