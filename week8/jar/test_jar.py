from jar import Jar

def main():


    test_init()
    test_str()
    test_depoist()
    test_withdraw()


def test_init():

    jar = Jar()
    assert jar.capacity == 12

    jar1 = Jar(5)

    assert jar1.capacity == 5



    ...


def test_str():

    jar = Jar()

    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"

    jar.withdraw

    ...


def test_deposit():

    jar = Jar()

    jar.deposit(7)

    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"

    ...


def test_withdraw():

    jar = Jar()

    jar.deposit(8)
    jar.withdraw(5)
    assert jar.size == 3

    ...

