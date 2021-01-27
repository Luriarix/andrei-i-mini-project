import csv


# 1. Create a CSV file with whatever data you choose. Read the file and print each row. Make sure you use headers!
with open("people.csv") as file:
    reader = csv.reader(file, delimiter=',')
    next(reader) # skips the header
    for row in reader:
        print(row)


# 2. Extend the above so that the data is read into a dictionary.
with open("people.csv") as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        print(row)


# 3. Write some data to a file. Choose whatever data you wish.
fieldnames = ['first_name', 'last_name', 'age']
people = (
    ['john', 'Smith', 20],
    ['sally', 'bloggs', 30],
    ['Jan', 'Smith', 60]
)

with open('people.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(people)



# 4. Write another block of code that will __append__ to the file created in #3.
with open('people.csv', mode='a', newline='') as file:
    fieldnames = ['first_name', 'last_name', 'age']

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writerow({'first_name': 'And','last_name': 'Drew','age': 27  })
