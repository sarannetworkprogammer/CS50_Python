def main():

    question = input("what is  the answer to the Great Question of Life, the Universe and Everything,? ").lower().strip()

    if question == "42" or question =="forty-two" or question == "forty two":
        print("Yes")
    else:
        print("No")


main()