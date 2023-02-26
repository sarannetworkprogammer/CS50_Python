from bank import value

def test_hello():
    assert value("HELLO") == 1

def test_how():
    assert value("How you doing") == 20

def test_happen():
    assert value("what's happening") == 100

def test_mixed():
    assert value("CS50") == 100
def test_num():
    assert value("100") == 100

