
a = ""
b = ""
temp = []
while True:

    str1 = "Adieu, adieu, to "
    try:
        name = input("Name: ")
        temp.append(name)

    except EOFError:
        #print(temp)
        print()

        if len(temp) == 1:

            a = a + temp[0]
            break

        if len(temp) > 1:


            for i in range(len(temp)-1):
                if len(temp) <= 2:
                    a = a + temp[i] + " "
                if len(temp) > 2:
                    a = a + temp[i] +", "
            b = "and "+ temp[len(temp)-1]

            break


print(str1+a+b)
