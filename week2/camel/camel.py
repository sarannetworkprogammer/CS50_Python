def main():

    camel_case = input("camelCase: ")
    temp =""
    for c in camel_case:
        if c.isupper():
            temp = temp + "_" + c.lower()
        else:
            temp = temp + c

    print(f"snake_case: {temp}")

if __name__ == "__main__":
    main()

