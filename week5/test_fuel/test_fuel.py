from fuel import convert, gauge
import pytest


def main():
    test_zero_division()
    test_value()
    test_valid_inputs()



def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')


def test_value():
    with pytest.raises(ValueError):
        convert("fox/dog")


def test_valid_inputs():
    assert convert('2/4') == 50 and gauge(50) == '50%'
    assert convert('1/100') == 1
    assert gauge(1) == 'E'
    assert convert('99/100') == 99
    assert gauge(99) == 'F'

if __name__ == "__main__":
    main()


