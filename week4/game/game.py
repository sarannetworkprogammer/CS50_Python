import random
import sys

# input for level

def level():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                return n
        except ValueError:
            pass

# taking input for guess

def guess():
    while True:
        try:
            guess_n = int(input("Guess: "))
            if guess_n > 0:
                break
        except ValueError:
            pass
    return guess_n


# passing input to compare

def compare(guess_n, number):

    if guess_n == number:
        print("Just right!")
        sys.exit()

    elif guess_n > number:
        print("Too large!")
        third(number)

    else:
        print("Too Small!")
        third(number)

#function for recurssion if it not satisfied

def third(number):
    guees_n = guess()
    compare(guees_n,number)



def main():
    n = level()
    number = random.randint(1,n)
    third(number)

main()
