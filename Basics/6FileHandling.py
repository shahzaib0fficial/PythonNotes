# Write in file
# a means Append

data = open("data.txt" , "a")

print("Enter Data to add in file")

data.write(input()) # in Append case it add text in the current text of file

data.close()

# w means Write
# it clears all the data which is in the file

data = open("data.txt" , "w")

data.write("This is a data in file") # we can also take data from user as upper

data.close()

#Read from file

data = open("data.txt" , "r")

print(data.read())

data.close()