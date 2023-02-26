import sys
from pyfiglet import Figlet
import random

#f = Figlet(font=sys.argv[2])

figlet= Figlet()

font_choice = random.choice(figlet.getFonts())


if len(sys.argv) == 1:
    f = Figlet(font=font_choice)
    plain_text = input("Input: ")
    print(f"Output: {f.renderText(plain_text)}")


elif len(sys.argv) == 3 and sys.argv[1] in ["-f","--font"] and sys.argv[2] in figlet.getFonts():
    f = Figlet(font=sys.argv[2])
    plain_text = input("Input: ")
    print(f"Output: {f.renderText(plain_text)}")


else:
    sys.exit("invalid usage")