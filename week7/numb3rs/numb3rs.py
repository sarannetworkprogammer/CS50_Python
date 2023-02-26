import re

import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):


    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$s",ip):
        octets = ip.split(".")
        count = 0
        #print(octets)
        for each_octet in octets:
            if int(each_octet) >= 0 and int(each_octet) <= 255:
                count = count + 1
        if count == 4:
            return True
        else:
            return False


    else:
        return False




if __name__ == "__main__":
    main()