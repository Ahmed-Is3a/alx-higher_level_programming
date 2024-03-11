#!/usr/bin/node

const argsCount = process.argv.length;

if (argsCount === 2) {
  console.log('No argument');
} else if (argsCount > 1) {
  console.log('Argument found');
}
