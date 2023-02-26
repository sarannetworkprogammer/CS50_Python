def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    count = 2
    a = 0
    if (len(s) <= 6 and s.isalnum() and s[0:2].isalpha() and len(s) >= 2 and s[2] != "0"):
        #print(type(s[2]))
        #print(s[0:2])



            #print("donothing")

            # do nothing
        if s[2:(len(s) - 1)].isdigit():
            return True

        elif s[2:(len(s) - 1)].isalnum():

                for letter in s[2:(len(s)-2)]:
                    count = count + 1
                    #print(letter)
                    if letter.isdigit:
                        #print("digit found")
                        #print("count",count)
                        if count+1 == (len(s)-1):
                            return True
                        if count+1 != (len(s)-1) and s[count+1: (len(s)-1)].isalpha():
                            #print(s[count+1: 6].isalpha())

                            #print("number should not be middle")
                            return True




    else:
        return False



if __name_ == "__main__":
    main()

