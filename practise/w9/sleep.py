# print n sheep

# generators generate values in function analyze lot of data , so much of information about

# yield taking one row at at time modifications 


def main():
    n = int(input("Whats n? "))

    flock = sheep(n)

    for s in flock:
        print(s)




def sheep(n):
    for i in range(n):
        yield ("🐑" * i)





if __name__ == "__main__":
    main()