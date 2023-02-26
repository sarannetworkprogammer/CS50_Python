def main():
    fraction = input("Fraction: ")
    percent = convert(fraction)
    output = gauge(percent)
    print(output)

def convert(fraction):
    while True:
        try:
            a = fraction.split("/")

            x= int(a[0])
            y= int(a[1])
            z = x / y

            if z <= 1:

                p = int(z * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError,ZeroDivisionError):
            raise

def gauge(percentage):

    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()