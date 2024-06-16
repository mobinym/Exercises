# scourgify.py
import sys
import os
import csv

def read_csv(input_file, output_file):
    if not input_file.endswith('.csv'):
        sys.exit("Not a CSV file")
    if not os.path.exists(input_file):
        sys.exit("File does not exist")
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['first', 'last', 'house'])
        for row in data[1:]:
            name = row[0].split(', ')
            writer.writerow([name[1], name[0], row[1]])

def main():
    if len(sys.argv) != 3:
        sys.exit("Invalid number of command-line arguments")
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    read_csv(input_file, output_file)

if __name__ == "__main__":
    main()
