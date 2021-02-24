
############################################################################

## What does this code do? 

# It opens/creates a file called "testFile.txt" in write mode. It then declares data in the form of a list, converts the list into a string format and writes that into the file, it then converts to a string and writes the declared dictionary to the file as well. The program then opens the file in read only mode, and prints the each line in the file one by one, as indicated by line = file.readline()

# file = open('testFile.txt', 'w')
# data = ['Grace', 9, 8, 10, 11]
# file.write(str(data) + '\n')

# myDictionary = {'name':'Grace', 'age':30}
# file.write(str(myDictionary) + '\n')

# file = open('testFile.txt', 'r')
# line = file.readline()
# print(line)
# line = file.readline()
# print(line)
# file.close()

############################################################################

## What does this code do? 

# Opens the testFile.txt in read only and stores its contents in the variable content. It then splits the content based on whether it starts on a new line. Enumerate adds a counter to the lines. If the word 'Grace' is found, it prints 'found' and adds the index position of the word to the list 'found'

# with open('testFile.txt', 'r') as file:
#     found = []
#     content = file.read()
#     lines = content.split('\n')
#     for pos, line in enumerate(lines):
#         if 'Grace' in line:
#             print('found')
#             found.append(pos)
#         else:
#             print('Not found')
#     print(found)

# ############################################################################

## What does this code do? 

# Opens the testFile.txt in read only mode, content is then saved as everything in the file. If the word 'Grace' is found inside the file, it will print 'found', if it's not, it'll print 'not found'

# with open('testFile.txt', 'r') as file:
#     content = file.read()
#     if 'Grace' in content:
#         print('found')
#     else:
#         print('Not found')

# ############################################################################

# ## What does this code do? 

# This opens the file as a read only file. It stores whatever is in the file to content and prints it. It then searches for the word 'Grace' in the file, and it has to match exactly as it is in order to find it (no lowercases). If it finds the word, it'll print 'found', if not, it prints 'Not found'

# import re

# with open('testFile.txt', 'r') as f:
#     content = f.read()
#     print(content)
#     regEx = re.search(r'Grace', content)
#     if regEx:
#         print('found')
#     else:
#         print('Not found')

############################################################################

##1 Write a simple algorithm that takes in a users name, age and hometown and write this to a file. Each users information should be on its own line. 

#Repeat the process 4 times, and then display the contents of the file in the command line when you are done. 

# counter = 0

# with open('usersInfo.txt', 'w') as file1:
#     while counter != 4:
#         try:
#             name = input("Please enter your name: ")
#             age = int(input("Please enter your age: "))
#             hometown = input("Please enter your hometown: ")
#             file1.write(f'{name},{str(age)},{hometown}\n')
#             counter += 1
#         except:
#             print("\n ***** Invalid age entered! *****")

# file1 = open('usersInfo.txt', 'r')
# contents = file1.read()
# print(contents)
# file1.close()

##2 Choose a poem of your choice and write it to a text file. Write an algorithm to count how many lines are in the poem. 

# with open('magiccity.txt') as file2:
#     counter = 0
#     content = file2.read()
#     lines = content.split('\n')
#     for line in lines:
#         if line:
#             counter +=1
#     print(f'The number of lines in "Magic City" is {counter}')

##3 Write a file with a list of song artists and song titles. Write an algorithm that will randomly display three of them from a list of at least 6. 

# import random

# with open('artists.txt') as file3:
#     artists = file3.read()
#     randomLine = artists.split('\n')
#     for choice in range(3):
#         randomChoice = random.choice(randomLine)
#         print(randomChoice)