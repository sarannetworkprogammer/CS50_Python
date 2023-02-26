"""
variable number of arguments are passed with * args
this is useful for scaling the code

map 
"""



def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()