import sys

file = sys.argv[1]

try:
    with open(file, "r") as f:
        content = f.read()
except:
    print(f"wc: {file}: No such file")
    exit(1)

lines = content.count("\n")
words = len(content.split()) if content.strip() else 0
bytes_ = len(content.encode())

print(f"{lines} {words} {bytes_} {file}")