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


def print_stdin():
    line_number = 1
    for line in sys.stdin:
        line = line.rstrip("\n")

        if args.b:
            if line != "":
                print(f"{line_number} {line}")
                line_number += 1
            else:
                print()
        elif args.n:
            print(f"{line_number} {line}")
            line_number += 1
        else:
            print(line)


def print_file(file, line_number):
    try:
        with open(file, "r") as f:
            for line in f:
                line = line.rstrip("\n")

                if args.b:
                    if line != "":
                        print(f"{line_number} {line}")
                        line_number += 1
                    else:
                        print()
                elif args.n:
                    print(f"{line_number} {line}")
                    line_number += 1
                else:
                    print(line)

    except:
        print(f"cat: {file}: No such file")

    return line_number


def main():
    line_number = 1

    if not args.files:
        print_stdin()
        return

    for file in args.files:
        line_number = print_file(file, line_number)


if __name__ == "__main__":
    main()