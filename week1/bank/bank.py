
def main():
    greet = input("Greeting: ").strip().lower()
    output = value(greet)
    print(type(output))


def value(greeting):


    if greeting.startswith("hello"):
        return 0

    elif greeting.startswith("h") and greeting !="hello" :
        return 20

    else:
        return 100



if __name__ == "__main__":
    main()