def main():

    dict1 = {}
    while True:
        try:
            item = input().upper()
            if item in dict1:
                dict1[item] = dict1[item] + 1
            else:
                dict1[item] = 1
        except EOFError:
            print()
            for key, value in sorted(dict1.items()):
                print(value, key)
            break

if __name__ == "__main__":
    main()