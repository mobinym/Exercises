from sys import argv
from random import choice
from pyfiglet import Figlet
import sys


figlet = Figlet()
#the getfont() method achive whole fonts in the Figlet() function
fontlist = figlet.getFonts()

#there is nothing except progaram name in command line
if len(sys.argv) == 1:
    #with fontset() method specify the font which it should be in random in output
    #with choice() method choose the random font from fontlist
    figlet.setFont(font = choice(fontlist))

#in this condition the command line has three correct arguments
elif len(sys.argv) == 3 or (str(argv[1] == "-f") or str(argv[1] == "--font")):
    # put a condition that argv[2] must be determined
    if str(argv[2]) in fontlist:
        # set a font for input which is equal to argv[2]
        figlet.setFont(font = str(argv[2]))
    #at this condition there is everything else in command line except the correct conditions above
    else:
        sys.exit("Invalid usage")
#at this condition the command line has more than 3 arguments
else:
    sys.exit("Invalid usage")

input = input("Input: ").strip()
#the rendertext() method make the font which is specified for the input
print(f"Output: {figlet.renderText(input)}")