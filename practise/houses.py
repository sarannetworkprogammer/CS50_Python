
# set eliminates the duplicates
#clean up for us
# Gloabl variables top of the file specific to module
# however  outside of those functions 

students = [
    {"name": "Heermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house":"Gryffindor"},
    {"name":"Draco", "house": "Slytherin"},
    {"name": "padma", "house": "Ravenclaw"},
]

houses = set()

for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)