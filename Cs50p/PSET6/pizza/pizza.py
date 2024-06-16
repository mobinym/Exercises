# pizza.py
import sys
import os
import csv
from tabulate import tabulate

def read_csv(filename):
    if not filename.endswith('.csv'):
        sys.exit("Not a CSV file")
    if not os.path.exists(filename):
        sys.exit("File does not exist")
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def main():
    if len(sys.argv) != 2:
        sys.exit("Invalid number of command-line arguments")
    filename = sys.argv[1]
    data = read_csv(filename)
    print(tabulate(data[1:], headers=data[0], tablefmt='grid'))

if __name__ == "__main__":
    main()
