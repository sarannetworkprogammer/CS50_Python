"""
Dictionary comphrension same data structure 

"""


students = ["Hermione", "Harry", "Ron"]


gryffindors = []


for student in students:
    gryffindors.append({"name":student, "house":"Gryffindor"})


print(gryffindors)