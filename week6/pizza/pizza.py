import sys
import csv
from tabulate import tabulate

def main():
    check_args(2,".csv")

    check_file()



def check_args(n,ext):
    if len(sys.argv) > n:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < n:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) == n:
        if not sys.argv[n-1].endswith(ext):
            sys.exit("Not a CSV file")



def check_file():

    try:
        with open(sys.argv[1],"r") as file:
            reader = csv.reader(file)
            table = reader
            #print(reader)


            print(tabulate(table, headers="firstrow",tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()