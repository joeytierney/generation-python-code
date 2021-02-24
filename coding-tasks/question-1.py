# Write an algorithm that takes 5 user input names and stores them into a list.
# Using this list, print out the name of the person who is first alphabetically.
# Ask the user to choose a name to replace, take a new name from the user and 
# store this in the same index location as the one being removed.
# 07/01/2021
# joey tierney

namesList = []

for x in range(5): # takes the users input 5 times
    name = input("Please enter a name: ")
    namesList.append(name) # stores users input into the list

namesList.sort() # sorts list alphabetically

print("The first name alphabetically in the list is: " + namesList[0])

nameReplace = input("Please enter a name to replace: ")

while nameReplace not in namesList: # while loop to ask user to enter a name if not in the list
    print("Sorry, could not find that name, try again")
    nameReplace = input("Please enter a name to replace: ")

location = namesList.index(nameReplace) # used to store the index of the item to be replaced

if nameReplace in namesList:
    newName = input("Please enter a new name: ")
    namesList.remove(nameReplace)
    namesList.insert(location, newName)

print(namesList)