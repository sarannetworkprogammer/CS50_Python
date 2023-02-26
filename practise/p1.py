def main():

    x = get_int("what is x")
    print(f" x is {x}")


def get_int(prompt):
    while True:

        try:
            x = int(input(prompt))
            return x

        except ValueError:
            pass



main()


