# lines.py
import sys
import os

def count_lines(filename):
    if not filename.endswith('.py'):
        sys.exit("Not a Python file")
    if not os.path.exists(filename):
        sys.exit("File does not exist")
    with open(filename, 'r') as file:
        lines = file.readlines()
    count = 0
    for line in lines:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith('#'):
            count += 1
    return count

def main():
    if len(sys.argv) != 2:
        sys.exit("Invalid number of command-line arguments")
    filename = sys.argv[1]
    print(count_lines(filename))

if __name__ == "__main__":
    main()
