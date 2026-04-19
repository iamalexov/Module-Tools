import sys
import os

args = sys.argv[1:]

flag_a = "-a" in args
flag_one = "-1" in args

paths = [arg for arg in args if arg not in ["-a", "-1"]]
path = paths[0] if paths else "."

try:
    files = os.listdir(path)
except:
    print(f"ls: cannot access '{path}'")
    exit(1)

files.sort()

if not flag_a:
    files = [f for f in files if not f.startswith(".")]

if flag_a:
    files = [".", ".."] + files

for file in files:
    print(file)