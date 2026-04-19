/* # Implement `cat`

You should already be familiar with the `cat` command line tool.

Your task is to implement your own version of `cat`.

It must act the same as `cat` would, if run from the directory containing this README.md file, for the following command lines:

/* `cat sample-files/1.txt`
/* `cat -n sample-files/1.txt`
/* `cat sample-files/*.txt`
/* `cat -n sample-files/*.txt`
/* `cat -b sample-files/3.txt`

Matching any additional behaviours or flags are optional stretch goals.

We recommend you start off supporting no flags, then add support for `-n`, then add support for `-b`.

 */
import fs from "fs";
import { program } from "commander";

program
  .option("-n")
  .option("-b")
  .argument("<files...>");

program.parse();

const options = program.opts();
const files = program.args;

let lineNumber = 1;

for (const file of files) {
  const content = fs.readFileSync(file, "utf-8");
  const lines = content.split("\n");

  for (const line of lines) {
    if (options.b) {
      if (line !== "") {
        console.log(lineNumber + " " + line);
        lineNumber++;
      } else {
        console.log("");
      }
    } else if (options.n) {
      console.log(lineNumber + " " + line);
      lineNumber++;
    } else {
      console.log(line);
    }
  }
}