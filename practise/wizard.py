#inheritance  properties from upper groups


class Wizard:

    def __init__(self,name):

        if not name:
            raise ValueError("Missing name")

        self.name = name



class Student(Wizard):

    def __init__(self,name,house):

        super().__init__(name)

        self.house = house


class Professor(Wizard):

    def __init__(self,name, subject):

        super().__init__(name)

        self.subject = subject


wizard = Wizard("Albus")

student = Student("Harry", "Gryffindor")

professor = Professor("Servus", "Defenses against Dark arts")

