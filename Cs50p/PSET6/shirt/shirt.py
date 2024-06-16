# shirt.py
import sys
import os
from PIL import Image, ImageOps

def overlay_shirt(input_file, output_file):
    if not input_file.lower().endswith(('.jpg', '.jpeg', '.png')) or not output_file.lower().endswith(('.jpg', '.jpeg', '.png')):
        sys.exit("Invalid input or output format")
    if not os.path.exists(input_file):
        sys.exit("Input file does not exist")
    if not input_file[input_file.rfind('.'):] == output_file[output_file.rfind('.'):]:
        sys.exit("Input and output have different extensions")
    shirt = Image.open('shirt.png')
    image = Image.open(input_file)
    image = ImageOps.fit(image, shirt.size)
    image.paste(shirt, (0, 0), shirt)
    image.save(output_file)

def main():
    if len(sys.argv) != 3:
        sys.exit("Invalid number of command-line arguments")
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    overlay_shirt(input_file, output_file)

if __name__ == "__main__":
    main()
