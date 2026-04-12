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

const files = program.args;



let lineNumber = 1;

for (const file of files) {
  const content = await fs.readFile(file, "utf-8");
  const lines = content.split("\n");

  for (const line of lines) {
    if (options.numberNonblank) {
      if (line.trim() !== "") {
        console.log(`${lineNumber}\t${line}`);
        lineNumber++;
      } else {
        console.log(line);
      }
    } else if (options.number) {
      console.log(`${lineNumber}\t${line}`);
      lineNumber++;
    } else {
      console.log(line);
    }
  }
}