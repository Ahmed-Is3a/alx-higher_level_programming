#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  let max = args[0];
  let secondMax = args[0];

  for (let i = 1; i < args.length; i++) {
    if (args[i] > max) {
      secondMax = max;
      max = args[i];
    } else if (args[i] > secondMax && args[i] < max) {
      secondMax = args[i];
    }
  }

  console.log(secondMax);
}
