import sys

args = sys.argv[1:]

flag_n = "-n" in args
flag_b = "-b" in args

files = [arg for arg in args if arg not in ["-n", "-b"]]
line_number = 1

for file in files:
    try:
        with open(file, "r") as f:
            lines = f.read().split("\n")
    except:
        print(f"cat: {file}: No such file")
        continue

    for line in lines:
        if flag_b:
            if line != "":
                print(f"{line_number} {line}")
                line_number += 1
            else:
                print("")
        elif flag_n:
            print(f"{line_number} {line}")
            line_number += 1
        else:
            print(line)