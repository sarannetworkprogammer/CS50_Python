from seasons import cal_minutes
from datetime import date



def test_oneyear():

    assert cal_minutes(date.fromisoformat("2021-07-16")) == "Five hundred twenty-five thousand, six hundred minutes"

def test_twoyear():

    assert cal_minutes(date.fromisoformat("2020-07-16")) == "One million, fifty-one thousand, two hundred minutes"

def main():
    
    test_oneyear()
    test_twoyear()


if __name__  ==  "__main__":
    main()