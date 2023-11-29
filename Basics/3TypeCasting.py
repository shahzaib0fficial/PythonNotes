# By default, input() returns a string so we need to convert in other data type according to the needs
print("Enter an Integer: ")

integer = int(input())

print("Enter an Float: ")

float = float(input())

print("Enter an String: ")

string = str(input())

print(f"Integer : {integer}, Float : {float}, String : {string}")

# We can also check the data type of a value

print("Enter an integer value : ")
value = int(input())
print(type(value))