#!/usr/bin/node

const arg = process.argv[2];

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  const size = parseInt(arg);
  if (size <= 0) {
    console.log('Invalid size');
  } else {
    for (let i = 0; i < size; i++) {
      let row = '';
      for (let j = 0; j < size; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
