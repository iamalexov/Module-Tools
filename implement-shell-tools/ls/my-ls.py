import sys
import os

args = sys.argv[1:]

path = args[0] if args else "."

try:
    files = os.listdir(path)
except:
    print(f"ls: cannot access '{path}'")
    exit(1)

files.sort()

for file in files:
    print(file)