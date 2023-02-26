# tupples are immutable you cannot change the value

# classes invent your data type

# attributes get inside something else instance variables inside of an object whose type is student

# methods functions inside class they are are special  standard function customize aka instance


class Student:
    # intialzation

    def __init__(self, name, house,):

        self.name = name
        self.house = house
    def __str__(self):

        return f"{self.name} from {self.house}"


    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name

    @property
    def house(self):
        return self._house
    @house.setter
    def house(self,house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():

    student = get_student()

    print(student)

def get_student():

    name = input("Name: ")
    house = input("House: ")

    return Student(name,house)



if __name__ == "__main__":
    main()