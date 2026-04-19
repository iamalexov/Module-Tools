import sys

args = sys.argv[1:]

flag_n = "-n" in args
flag_b = "-b" in args

files = [arg for arg in args if arg not in ["-n", "-b"]]
