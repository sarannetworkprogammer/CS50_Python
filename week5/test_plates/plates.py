

def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6 or s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    i = 0

    while i <= len(s)-1:
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i = i + 1


    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    for letter in s:
        if letter in [".", " ", "!", "?"]:
            return False

    return True







if __name__ == "__main__":
    main()
