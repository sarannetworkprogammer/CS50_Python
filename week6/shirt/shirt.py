from PIL import Image, ImageOps
import sys
import os


def validations():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv)  == 3:
        # splitting the extensions

        if os.path.exists(sys.argv[1]) == True:


            a = os.path.splitext(sys.argv[1])
            b = os.path.splitext(sys.argv[2])
            if (a[1].lower() == b[1].lower()) and a[1].lower() in [".jpg",".png",".jpeg"]:

                #print("same extension")
                return True


            elif (a[1].lower() != b[1].lower()) and a[1].lower() and b[1].lower() in [".jpg",".png",".jpeg"]:
                sys.exit("Input and output have different extensions")

            else:
                sys.exit("Invalid input")
        else:

            sys.exit("Input doesnot exist")


    return False


def img_operations():

    try:

        image1 = Image.open(sys.argv[1])

        shirt = Image.open("shirt.png")

        size = shirt.size

        image1 = ImageOps.fit(image1, size)

        image1.paste(shirt, shirt)

        image1.save(sys.argv[2])

    except:
        sys.exit("File not found")



def main():

    x = validations()
    #print(x)

    if x == True:
        img_operations()



if __name__ == "__main__":
    main()




