import re

##opening a file, reading each line and splitting it up to search each item/ display only certain items at the end  

# file = open("people.txt", "r")
# for loop in range(4):
#     line = file.readline()
#     data = line.split(",")
#     isMusician = re.match(r'Musician', data[2])
#     if isMusician:
#         print(data[0],data[1])
# file.close()

#######################################################

#opening a file, reading each line, searching for musician and printing the whole line 

# file = open("people.txt", "r")
# for loop in range(4):
#     line = file.readline()
#     isMusician = re.search(r'Musician', line)
#     if isMusician:
#         print(line)
# file.close()

###########################################################

##counting how many lines are in the file by reading whole file, splitting at \n and counting the total lines

# with open('people.txt') as f:
#     counter = 0
#     content = f.read()
#     lines = content.split('\n')
#     for i in lines:
#         if i:
#             counter += 1
#     print(f'Number of lines in the file {counter}')

##the first algorithm taking counter instead of a hardcoded number. 

# file = open("people.txt", "r")
# for loop in range(counter):
#     line = file.readline()
#     data = line.split(",")
#     isMusician = re.match(r'Musician', data[2])
#     if isMusician:
#         print(data[0],data[1])
# file.close()

###########################################################
    
##counting how many lines are in the files a more simple way

# with open('people.txt') as myfile:
#     counter = 0
#     for line in myfile:
#         if line:
#             counter += 1
    
#     print(f'Number of lines in the file {counter}')


##Using line count and combining with search algorithm 

# with open('people.txt') as myfile:
#     counter = 0
#     for line in myfile:
#         if line:
#             counter += 1
#             data = line.split(",")
#             isMusician = re.match(r'Musician', data[2])
#             if isMusician:
#                 print(data[0],data[1])
    
#     print(f'Number of lines in the file {counter}')
    






