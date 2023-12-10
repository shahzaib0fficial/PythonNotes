import csv

fields = ["Name","Degree","CGPA"]

data = [
    ["AbdulAleem","BSCS","4.0"],
    ["Shahzaib","BSCS","3.5"],
    ["UmarDraz","BSCS","3.0"],
    ["Muhannad","BSCS","2.5"]
]

with open("csvFile.csv","w",newline="") as file:
    writer = csv.writer(file)

    writer.writerow(fields)
    writer.writerows(data)

dataOfCsvFile = []

with open("csvFile.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        dataOfCsvFile.append(row)

for data in dataOfCsvFile:
    print(data)