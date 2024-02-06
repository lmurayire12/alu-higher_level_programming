#!/usr/bin/node

const fs = require("fs");
const filePath = process.argv[2];

fs.readFile(filePath, "utf-8", (error, fileContent) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  console.log(fileContent);
});
