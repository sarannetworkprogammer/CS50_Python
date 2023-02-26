from plates import is_valid

def test_plate():
    assert is_valid("CS50") == True
    assert is_valid("AA3344") == True
    assert is_valid("BB") == True
    assert is_valid("CDD2") == True

def test_invalid():
    assert is_valid("PI3.14") == False
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False
    assert is_valid("He4E") == False
    assert is_valid("22") == False


def test_words():
    assert is_valid("OUTATIME") == False

def test_letter():
    assert is_valid("H") == False


def main():
    test_plate()
    test_invalid()
    test_words()
    test_letter()


if __name__ == "__main__":
    main()