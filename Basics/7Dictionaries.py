#first way of difining dictionary

student = {
    "name" : "Shahzaib",
    "age" : 19,
    "friend" : ["AbdulAleem","Umar Draz","Muhannad"]
}

#second way of difining dictionary

#student = dict(name = "Shahzaib", age = 19, friend = ["AbdulAleem","Umar Draz","Muhannad"])

#first method of adding new key value pair or updating

student["degree"] = "Bscs"

#second method of adding new key value pair or updating

student.update({"degree" : "BSCS"})

for std in student:
    if type(student[std]) != list:
        print(f"{std} : {student[std]}")
    else:
        for value in student[std]:
            print(f"{std} : {value}")


#remove last key value pair

student.popitem()

#print whole dictionary

print(student)

#remove specific key value pair

student.pop("age")

#print whole dictionary

print(student)

#clear all data from dictionary

student.clear()

#print whole dictionary

print(student)