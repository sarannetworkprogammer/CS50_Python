"""
Implemented basic caeser encryption decryption function

"""

import sys

def main():

    # first checking validations
    output = validations()
    output1 = display_out(output)
    print(output1)


# encrypt function takes input of plaintext and key and gives output of encrypted text
def encrypt(text, key):

    res = ""

    for i in range(len(text)):
        c = text[i]

        if c.isupper():
            res = res+ chr((ord(c) + key -65) % 26 + 65)
        elif c.islower():
            res = res + chr((ord(c) + key - 97) % 26 + 97)
        else:
            res = res + c

    return res


# decrypt function: takes input of cipher text, key and gives ouptut of plain text

def decrypt(text, key):

    res = ""

    for i in range(len(text)):
        c = text[i]

        if c.isupper():
            res = res+ chr((ord(c) - key -65) % 26 + 65)
        elif c.islower():
            res = res + chr((ord(c) - key - 97) % 26 + 97)
        else:
            res = res + c

    return res




def take_input():

    plain_text = input("Text: ")

    try:
        key = int(input("Key: "))
    except:
        pass

    return plain_text, key


# validation function minimum length of args should be two either encrytpion or decryption.

def validations():


    if len(sys.argv) == 2:

        if (sys.argv[1]) == "-e":
            text, key = take_input()
            encrypted_text = encrypt(text,key)
            return encrypted_text

        elif (sys.argv[1]) == "-d":
            text, key = take_input()
            decrypted_text = decrypt(text, key)
            return decrypted_text
        else:
            sys.exit("Usuage: python file.py e")
    else:
        sys.exit("Usuage: python file.py e or d")



def display_out(output):

    return f"Output: {output}"


if __name__ == "__main__":
    main()