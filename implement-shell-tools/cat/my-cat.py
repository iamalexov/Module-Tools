import sys

args = sys.argv[1:]

flag_n = "-n" in args
flag_b = "-b" in args

files = [arg for arg in args if arg not in ["-n", "-b"]]

line_number = 1

for file in files:
    try:
        with open(file, "r") as f:
            for line in f:
                if flag_b:
                    if line.strip() != "":
                        print(f"{line_number:6}  {line}", end="")
                        line_number += 1
                    else:
                        print(line, end="")
                elif flag_n:
                    print(f"{line_number:6}  {line}", end="")
                    line_number += 1
                else:
                    print(line, end="")
    except FileNotFoundError:
        print(f"cat: {file}: No such file or directory", file=sys.stderr)