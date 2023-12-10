import sys

names = ["AbdulAleem", "Shahzaib", "UmarDraz",]

print("Enter name you wanna to search: ", end="") #end by default value is \n
name = input()

if name in names: #do linear search in a list
    print("Found")
    sys.exit(0)

print("Not Found")
sys.exit(1)