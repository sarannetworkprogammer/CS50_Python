from datetime import date
import sys
import inflect

p = inflect.engine()

def main():

    try:
        d0 = date.fromisoformat(input("enter the date = "))

        print(cal_minutes(d0))


    except ValueError:
        sys.exit("Invalid date")


def cal_minutes(d0):


    d1 = date.today()
    delta = d1 - d0
    days_number =  delta.days
    minutes_number = days_number *(24*60)
    words = p.number_to_words(minutes_number, andword="")
    return words.capitalize() + " minutes"


if __name__ == "__main__":
    main()