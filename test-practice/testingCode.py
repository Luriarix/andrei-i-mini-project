people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]




# #1
# file = open('people.txt', 'w')
# for item in people:
#     file.write(f'{item}\n')
# file.close()


#2
# try:
#     file = open('people.txt', 'w')
#     for item in people:
#         file.write(f'{item}\n')
#     file.close()
# except: 
#     print("Error...Error...ERROR...ERROR...")
#     file.close()


# #3
# try:
#     file = open('people.txt', 'w')
#     for item in people:
#         file.write(f'{item}\n')
# except: print("Error...Error...ERROR...ERROR...")
# finally: file.close()


# #4
# with open('people.txt', 'w+') as file:
#     for item in people:
#         file.write(f'{item}\n')


# #5
# temp = []
# uniqI = {}

# with open('people2.txt', 'r') as people:
#     for item in people:
#         temp.append(item)

# for item in temp:
#     if item not in uniqI.keys():
#         uniqI[item] = temp.count(item)

# for item in uniqI.items():
#     print(f"key: {item[0].rstrip()}, count: {item[1]}")

#  #5 alt
# with open('people2.txt', 'r') as people:
#     for item in people:
        # if item in uniqI.keys():
            # uniqI[item] += 1
        # else: uniqI[item] = 1