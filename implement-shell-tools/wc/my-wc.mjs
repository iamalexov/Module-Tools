import fs from "fs";

const args = process.argv.slice(2);

let flagL = false;
let flagW = false;
let flagC = false;

const files = [];

for (const arg of args) {
  if (arg === "-l") flagL = true;
  else if (arg === "-w") flagW = true;
  else if (arg === "-c") flagC = true;
  else files.push(arg);
}

if (!flagL && !flagW && !flagC) {
  flagL = true;
  flagW = true;
  flagC = true;
}

let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;

for (const file of files) {
  let content;

  try {
    content = fs.readFileSync(file, "utf-8");
  } catch {
    console.error(`wc: ${file}: No such file`);
    continue;
  }

  const lines = content.split("\n").length - 1;
  const words = content.trim() === "" ? 0 : content.trim().split(/\s+/).length;
  const bytes = Buffer.byteLength(content);

  totalLines += lines;
  totalWords += words;
  totalBytes += bytes;

  let output = "";

  if (flagL) output += lines + " ";
  if (flagW) output += words + " ";
  if (flagC) output += bytes + " ";

  console.log(output + file);
}

if (files.length > 1) {
  let totalOutput = "";

  if (flagL) totalOutput += totalLines + " ";
  if (flagW) totalOutput += totalWords + " ";
  if (flagC) totalOutput += totalBytes + " ";

  console.log(totalOutput + "total");
}