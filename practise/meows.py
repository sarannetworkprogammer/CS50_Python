''' accessing constants inside class
Here we define constants with upper case only

'''

class Cat:
    MEOWS = 3


    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")



cat = Cat()

cat.meow()