import sys

args = sys.argv[1:]

flag_l = "-l" in args
flag_w = "-w" in args
flag_c = "-c" in args

files = [arg for arg in args if arg not in ["-l", "-w", "-c"]]

if not flag_l and not flag_w and not flag_c:
    flag_l = flag_w = flag_c = True

total_l = total_w = total_c = 0

for file in files:
    try:
        with open(file, "r") as f:
            content = f.read()
    except:
        print(f"wc: {file}: No such file")
        continue

    lines = content.count("\n")
    words = len(content.split()) if content.strip() else 0
    bytes_ = len(content.encode())

    total_l += lines
    total_w += words
    total_c += bytes_

    output = ""
    if flag_l:
        output += f"{lines} "
    if flag_w:
        output += f"{words} "
    if flag_c:
        output += f"{bytes_} "

    print(output + file)

if len(files) > 1:
    total_output = ""
    if flag_l:
        total_output += f"{total_l} "
    if flag_w:
        total_output += f"{total_w} "
    if flag_c:
        total_output += f"{total_c} "

    print(total_output + "total")