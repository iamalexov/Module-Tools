#!/usr/bin/env node

import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .option("-l", "lines")
  .option("-w", "words")
  .option("-c", "chars")
  .argument("<files...>");

program.parse();

const options = program.opts();
const files = program.args;

let totalL = 0;
let totalW = 0;
let totalC = 0;

for (const file of files) {
  try {
    const content = await fs.readFile(file, "utf-8");

    const lines = content.split("\n").length - 1;
    const words = content.trim() ? content.trim().split(/\s+/).length : 0;
    const chars = content.length;

    totalL += lines;
    totalW += words;
    totalC += chars;

    let result = "";

    if (!options.l && !options.w && !options.c) {
      result = `${lines} ${words} ${chars}`;
    } else {
      if (options.l) result += `${lines} `;
      if (options.w) result += `${words} `;
      if (options.c) result += `${chars} `;
    }

    console.log(result + file);

  } catch (err) {
    console.log(`wc: ${file}: error`);
  }
}

// total если несколько файлов
if (files.length > 1) {
  let result = "";

  if (!options.l && !options.w && !options.c) {
    result = `${totalL} ${totalW} ${totalC}`;
  } else {
    if (options.l) result += `${totalL} `;
    if (options.w) result += `${totalW} `;
    if (options.c) result += `${totalC} `;
  }

  console.log(result + "total");
}