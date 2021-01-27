import csv


# 1. Create a CSV file with whatever data you choose. Read the file and print each row. Make sure you use headers!
with open("people.csv") as file:
    reader = csv.DictReader(file, delimiter=',')
    # next(reader) # skips the header
    for row in reader:
        print(row)


# 2. Extend the above so that the data is read into a dictionary.
with open("people.csv") as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        print(row)


# 3. Write some data to a file. Choose whatever data you wish.
fieldnames = ['first_name', 'last_name', 'age']
people = [
    ['john', 'Smith', 20],
    ['sally', 'bloggs', 30],
    ['Jan', 'Smith', 60]
]

with open('people.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(fieldnames)
    writer.writerows(people)



# 4. Write another block of code that will __append__ to the file created in #3.
with open('people.csv', mode='a') as file:
    writer = csv.writer(file, delimiter=',')

    writer.writerow(['And', 'Drew', 27])
