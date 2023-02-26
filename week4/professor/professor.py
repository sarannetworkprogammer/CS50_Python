import random

def main():
    level = get_level()
    score = track(level)
    print("score:", score)


    #print(x,y)


    # printing score
    #print(score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
            pass
    return level

def generate_integer(n):

    if n == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    else:

        range_start = 10**(n-1)
        range_end = (10**n)-1
        x = random.randint(range_start, range_end)
        y = random.randint(range_start, range_end)
    return x,y

def question_display(x,y):
    count_chance = 1

    while count_chance <= 3:

        try:
            ans = int(input(f"{x} + {y} = "))
            if ans == x + y:
                #print("sucess")
                return True
            else:
                count_chance = count_chance + 1
                print("EEE")
        except:
            print("EEE")
            count_chance = count_chance + 1
            pass

    print(f"{x} + {y} = {x+y}")

    return False



def track(level):
    count_round = 0
    score =0
    while count_round < 10:
        x,y = generate_integer(level)
        check_answer = question_display(x,y)
        if check_answer == True:
            score = score +1
        count_round = count_round + 1

    return score






if __name__ == "__main__":
    main()

