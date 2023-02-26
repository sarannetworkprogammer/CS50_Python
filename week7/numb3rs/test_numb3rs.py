from numb3rs import validate
import re


def test_words():
    assert validate(r"hello")  == False
    assert validate(r"cat")  == False
def test_all_octets():
    assert validate(r"192.168.1.1")  == True
    assert validate(r"10.10.10.10")  == True
def test_three_octets():
    assert validate(r"1.1.1")  == False
    assert validate(r"2.2.2")  == False
    assert validate(r"1") == False
def test_mix():
    assert validate(r"1.1.1.cat") == False
def test_outside_range():
    assert validate(r"285.236.39.31") == False


def main():
    test_mix()
    test_three_octets()
    test_all_octets()
    test_words()
    test_outside_range()

if __name__ ==  "__main__":
    main()




