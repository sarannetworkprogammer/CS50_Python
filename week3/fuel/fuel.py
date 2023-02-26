
"""

while True:
    try:
        fraction = input("Fraction: ")
        a = fraction.split("/")
    #print(a)
        if int(a[0]) >= 0 and int(a[1]) > 0 and int(a[0]) <= int(a[1]):
            break
    except ValueError:
        print("value error")



z = int(a[0])/int(a[1])
c = round(z * 100)
 #print(c)
if c <= 1.0:
    print("E")
elif c >= 99.0:
    print("F")
else:
    print(str(int(c)) + "%")


"""



def convert(fraction):

    while True:
        try:
            a,b = fraction.split("/")
            print(a)
            x = int(a)
            #print(x)
            y = int(b)
            #print(y)
            z = x / y
            #print(z)
            if z <= 1:
                p = int(z * 100)
                #print(p)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError,ZeroDivisionError):
            raise




def guage(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


def main():

     fraction = input("Fraction: ")
     percent = convert(fraction)
     #print(percent)
     output = guage(percent)
     print(f"output:{output}")


if __name__ == "__main__":
    main()

