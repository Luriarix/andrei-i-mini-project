import csv
with open("testing.csv") as file:
    # reader = csv.reader(file, delimiter=',')
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        print(row)