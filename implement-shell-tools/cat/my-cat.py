import sys
import argparse


parser = argparse.ArgumentParser(
    prog="cat",
    description="Concatenate files and print on the standard output"
)

parser.add_argument("files", nargs="*", help="Files to read")
parser.add_argument("-n", action="store_true", help="Number all output lines")
parser.add_argument("-b", action="store_true", help="Number non-blank lines")

args = parser.parse_args()

def main():
    line_number = 1

    if not args.files:
        print_stdin()
        return

    for file in args.files:
        line_number = print_file(file, line_number)


if __name__ == "__main__":
    main()