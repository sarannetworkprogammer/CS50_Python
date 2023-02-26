from um import count



def test_present():
    assert count("hello, um")  == 1
def test_presenttwice():
    assert count("um,um, yummy") == 2
def test_absent():
    assert count("yummy")  == 0



def main():
    test_present()
    test_presenttwice()
    test_absent()



if __name__ == "__main__":
    main()