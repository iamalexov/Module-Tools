#!/usr/bin/env node

import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .option("-1", "one file per line")
  .option("-a", "show hidden files")
  .argument("[dir]", "directory", ".");

program.parse();

const options = program.opts();
const dir = program.args[0] || ".";
try {
  let files = await fs.readdir(dir);

  if (!options.a) {
    files = files.filter(file => !file.startsWith("."));
  } else {
    files = [".", "..", ...files];
  }

  files.sort();

  if (options["1"]) {
    for (const file of files) {
      console.log(file);
    }
  } else {
    console.log(files.join(" "));
  }

} catch (error) {
  console.error(`ls: cannot access '${dir}': ${error.message}`);
}