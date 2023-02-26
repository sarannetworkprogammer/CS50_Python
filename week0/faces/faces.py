
def check_emoji(sentence):

    if ":)" or ":(" in sentence:
        sentence = sentence.replace(":)","🙂")
        sentence= sentence.replace(":(","🙁")

    return sentence


def main():
    sentence = input()
    new_sentence = check_emoji(sentence)
    print(new_sentence)


if __name__ == "__main__":
    main()





