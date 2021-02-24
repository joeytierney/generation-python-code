# Write an algorithm that takes a name, the age and height (in cm) of 5 people. 
# The age and height should be integers. Each set of data should be stored within a 2D list.
# ask a user for a name and return the name, age and height for that person in a formatted string.
# Calculate the average age for all the users.
# Calculate the difference between the tallest person and the shortest person.
# Return the data of three oldest people.
# 07/01/2021
# joey tierney

peopleList = []
sum = 0

for x in range(5): # take 5 inputs from the user
    name = input("Please enter a name: ")
    age = int(input("Please enter their age: "))
    height = int(input("Please enter their height: "))
    usersList = [name, age, height] # store these inputs into a list
    peopleList.append(usersList) # add that list into the 2d list

print(str(peopleList)[1:-1]) # print the list as a String

# print(peopleList[0][1])
# print(peopleList[1][1])
# print(peopleList[2][1])
# print(peopleList[3][1])
# print(peopleList[4][1])

for col in range(len(peopleList)):
    for item in range(len(col)):
        print(col[item])