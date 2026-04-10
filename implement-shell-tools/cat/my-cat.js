#!/usr/bin/env node
import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("my-cat")
  .description("Reimplementation of cat")
  .option("-n, --number", "number all lines")
  .option("-b, --number-nonblank", "number non-empty lines")
  .argument("<files...>", "files to read");

program.parse();

const options = program.opts();
console.log('Options: ', options);

const files = program.args;
console.log('Files: ', files);

for (const file of files) {
  const content = await fs.readFile(file, "utf-8");
  console.log(content);
}