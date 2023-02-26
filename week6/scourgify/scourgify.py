import sys
import csv



def main():
    check_args(3,".csv")
    read_write()




def check_args(n,ext):
    if len(sys.argv) > n:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < n:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) == n:
        if not sys.argv[n-1].endswith(ext):
            sys.exit("Not a CSV file")

def read_write():
    try:
        with open(sys.argv[1]) as file1:
            reader = csv.DictReader(file1)
            with open(sys.argv[2], "w") as file2:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(file2, fieldnames = fieldnames)
                writer.writeheader()
                for row in reader:
                    writer.writerow({"first" : row["name"].split(",")[1].lstrip(), "last" : row["name"].split(",")[0], "house" : row["house"]})
    except FileNotFoundError:
        sys.exit("File doesnot exist")







if __name__  ==  "__main__":
    main()