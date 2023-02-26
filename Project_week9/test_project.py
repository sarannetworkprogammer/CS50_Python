from project import encrypt, decrypt, display_out


def main():
    ...
    test_encrypt()
    test_decrypt()
    test_display_out()



def test_encrypt():

    encrypt("abc",3) == "def"
    encrypt("abc", 3) == "def 50"


def test_decrypt():

    decrypt("abc",3) == "xyz"
    decrypt("def 50",3) == "def 50"

def test_display_out():
    display_out("abc") == "Output: def"


if __name__ == "__main__":
    main()
