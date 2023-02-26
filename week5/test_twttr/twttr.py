
def main():
    word = input("Input: ")
    print(f"Output:", shorten(word))


def shorten(word):
    output = ""
    for letter in word:
        if letter.lower() not in ["a","e","i","o","u"]:
            output = output + letter
    return output



if __name__ == "__main__":
    main()