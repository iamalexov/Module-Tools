import sys

files = sys.argv[1:]

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

    print(f"{lines} {words} {bytes_} {file}")

if len(files) > 1:
    print(f"{total_l} {total_w} {total_c} total")