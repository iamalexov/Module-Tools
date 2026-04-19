import fs from "fs";

const args = process.argv.slice(2);

let flagA = false;
let path = ".";

for (const arg of args) {
  if (arg === "-a") {
    flagA = true;
  } else if (arg === "-1") {
  } else {
    path = arg;
  }
}

let files;

try {
  files = fs.readdirSync(path);
} catch (err) {
  console.error(`ls: cannot access '${path}': No such file or directory`);
  process.exit(1);
}

if (!flagA) {
  files = files.filter(file => !file.startsWith("."));
}

files.sort();

if (flagA) {
  files.unshift(".", "..");
}

for (const file of files) {
  console.log(file);
}