'''
list1 = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
#print(list1.index("January") + 1)
#date = input("Date: ").split("/")


n=24
print(f"{n:02}")


#print(date)

#if date.isdigit():
#    print("yes")

#    if int(date[1]) > 0 and int(date[1]) <= 31 and int(date[0]) > 0 and int(date[0]) <= 12:

 #       print(date[2]+ "-" + date[1] + "-" + date[0])
 '''



#print(f"date: {date}")
# fist format


'''
while True:
    date = input("Date: ").split("/")

    if int(date[1]) > 0 and int(date[1]) <= 31 and int(date[0]) > 0 and int(date[0]) <= 12:

        print(str(date[2]).zfill(4)+ "-" + str(date[1]).zfill(2) + "-" + str(date[0]).zfill(2))
        break

'''

# format




list1 = ["January", "February", "March","April", "May", "June", "July", "August", "September", "October", "November", "December"]





def format(s):


    try:

        if "," in s:
            date = s.split(",")
            p = date[0].split()
            #print(p[0])
            #print(list1.index(str(p[0])))

            m = list1.index(str(p[0])) + 1

            if int(p[1]) > 0 and int(p[1]) <= 31 and p[0] in list1 :

                print(str(date[1]).zfill(4).strip()+ "-" +str(m).zfill(2) + "-" + str(p[1]).zfill(2))

            else:
                main()


        elif "/" in s :

            date = s.split("/")

            if int(date[1]) > 0 and int(date[1]) <= 31 and int(date[0]) > 0 and int(date[0]) <= 12:

                print(str(date[2]).zfill(4).strip()+ "-" +str(date[0]).zfill(2).strip()+ "-" +str(date[1]).zfill(2))
            else:
                main()
        else:
            main()
    except:
        main()


def main():

    s = input("Date:").strip()
    format(s)



if __name__ == "__main__":
    main()



