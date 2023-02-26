
def main():
    greet = input("Greeting: ").strip().lower()
    output = value(greet)
    print(output)


def value(greeting):


    if greeting.strip().lower().startswith("hello"):
        return 0

    elif greeting.strip().lower().startswith("h") and greeting !="hello" :
        return 20

    else:
        return 100



if __name__ == "__main__":
    main()