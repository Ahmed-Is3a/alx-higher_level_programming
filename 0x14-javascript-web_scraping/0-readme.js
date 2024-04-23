#!/usr/bin/node
// reads and prints the content of a file

const filesys = require('fs'); // fs = file system
filesys.readFile(process.argv[2], 'utf-8',
  function (err, data) {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });
