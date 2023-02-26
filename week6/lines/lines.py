import sys

import os.path


def main():
    check_args()

    if len(sys.argv) == 2 and sys.argv[1].endswith(".py") and os.path.isfile(sys.argv[1]) :

        count = 0
        comment = 0
        space = 0

        try:
            with open(sys.argv[1]) as file:
                for line in file:
                    if line.strip():
                        count = count + 1
                    if line.lstrip().startswith("#") is True:
                        comment = comment + 1


            total = count - comment -space
            print(f"{total}")
        except FileNotFoundError:
            sys.exit("File doesnot exist")



def check_args():

# checking command line arguments


    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if  not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    if os.path.exists(sys.argv[1]) == False:
        sys.exit("File does not exist ")




if __name__ == "__main__":
    main()


