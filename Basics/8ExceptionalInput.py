print("Enter an Integer")

while True:
    #try to take an value and convert in intger type if have any issue it goes to except case and run
    try:
        a = int(input())
        break
    except ValueError:
        print("Please Input an Integer")

print(f"The value you intereg is {a}")

#it can work for any type of exceptional error
#like if the variable is not define and we are trying to print 
#also if the file is not opening we file dosen't exist we can deal such cases with that