import re

#1 - Write a regular expression that will accept an irish landline number. 

userNum = input("Please enter your phone number: ")
validNum = re.match(r'\d{9})$', userNum)

if validNum:
    print("Valid Irish landline")
else:
    print("Invalid number")

################################################################################
#2 - Write an expression that will search for any irish mobile numbers, provide a test string with a couple of numbers. 

mobileNums = "0859182011. 0481234567. 0861112678. 0830071293. 0895438901. 01234519. 0851234"

findNums = re.findall('08\d{8}', mobileNums)

print(findNums)

################################################################################
#3 - Write a simple program that asks a user if they are in the ROI or NI, and then get them to input the correct postcode (eircode) accordigly.

validLoc = False

while not validLoc:
    askUserLoc = input("Are you in ROI or NI? ")
    if askUserLoc == "ROI":
        askPostCode = input("Please enter your postcode: ")
        validPostCode = re.match(r'[A-Y]{1}\d{2}\s[A-Z0-9]{4}$', askPostCode)
        if validPostCode:
            print("Valid Post Code")
            validLoc = True
        else:
            print("Invalid Post Code")
    elif askUserLoc == "NI":
        askPostCode = input("Please enter your postcode: ")
        validPostCode = re.match(r'([BT]+[0-9]{2}$)', askPostCode)
        if validPostCode:
            print("Valid Post Code")
            validLoc = True
        else:
            print("Invalid Post Code")
    else:
        print("Please enter ROI or NI")

################################################################################
#4 - Write an expression that checks if a memeber of staff has a legitimate generation email. Generation emails are normally always <firstname>.<surname>@generation.org, however some staff are simply <firstname>@generation.org 



################################################################################
#5 - Write an expression to validate a DOB. It will either be for example: 07/03/1990 or 07/03/90. It must be in one of these formats.          
dob = False

while not dob:
    askDOB = input("Please enter your Date of Birth (DD/MM/YYYY): ")
    validDOB = re.match(r'^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$', askDOB)

    if validDOB:
        print("Valid Date of Birth entered")
        dob = True
    else:
        print("Invalid Date of Birth entered")

################################################################################



#Instructors code 

#import re


#########################################################################


# name = input("Enter your name: ")
# valid = re.match("[A-Z]",name)
# if valid:	
#     print("That looks OK")
# else:
#  	print("Invalid, no capital")

##########################################################################


# numText = 'My telephone number is 07598345903. My mums numbers 07756235412.'
# # phoneNumber = input('Enter your number: ')
# numbers = re.search(r'07\d{9}', numText)
# print(numbers)
# # number = numText[23:34]
# # print(number)

##########################################################################


# ## match() will start looking at the start of the string 
# numText = 'My telephone number is 07598345903. My mums numbers 07756235412.'
# isNumValid = re.match(r'07\d{09}', numText) #will return false
# print(bool(isNumValid))

# isNumValid = re.match(r'.+07\d{09}', numText) #will return true
# print(str(bool(isNumValid)))


#########################################################################

# ##findall()
# numText = 'My telephone number is 07598345903. My mums numbers 07756235412.'
# # phoneNumber = input('Enter your number: ')
# isNumValid = re.findall(r'07\d{09}', numText)
# print(isNumValid)
# #output will be - ['07598345903', '07756235412']


##########################################################################

# fileName = 'file1, file2, file33, 3files, 13_files'
# fileFound = re.findall(r'file', fileName)
# fileFound = re.findall(r'.file', fileName)
# fileFound = re.findall(r'\wfile', fileName)
# fileFound = re.findall(r'\w+file', fileName)
# fileFound = re.findall(r'[a-z0-9_]*file', fileName)
# fileFound = re.findall(r'\dfile', fileName)
# fileFound = re.findall(r'file\d+', fileName)
# fileFound = re.findall(r'file\d{2}', fileName)
# fileFound = re.findall(r'.files?', fileName)
# fileFound = re.findall(r'.+files?', fileName)

# print(fileFound)

##########################################################################

# ##valid characters a-z, A-Z, 0-9 !$%?@ - 6-10 characters in length

# while(1):
#     passwordIn = input('What password would you like to add? ')
#     isValid = re.match(r'^[a-zA-Z0-9!$%?@]{6,10}$', passwordIn)

#     if isValid:
#         print('Valid')
#     else:
#         print('Not valid')

##########################################################################

# testString = 'This is a standard string. It has all the usual punctuation marks! I should probably delete them...'
# # regEx = re.findall(r'[^!_.?]+', testString)
# # print(regEx)

# #remove the spaces 
# clean = re.findall(r'[^!_.?]+', testString) #with space
# print(clean)
# newstring = ' '.join(clean) #rejoins the words
# print(newstring)

##########################################################################


# import re	


# ##########################################################################



# # #program checks that userID entered has one or more uppercase letter
# # #followed by three digits

# # while(1):
# #     userID = input("Enter your user ID: \n")
# #     isValidID = re.match(r'^[A-Z]{1,2}[0-9]{3}$', userID)


# #     if isValidID:
# #         print('Valid ID \n')
# #     else:
# #         print('Invalid ID \n')


# ##########################################################################


# # #A product code starts with one or two uppercase letters 
# # # followed by four or more digits and end with either 
# # # H or G

# # print('''A product code starts with one or two uppercase letters, \n followed by four or more digits and end with either H or G''')

# # productCode = input('Enter a valid product code (type "x" to end) \n')

# # while productCode != 'x':
# #     isValid = re.match('^[A-Z]{1,2}[0-9]{4,}[HG]$', productCode)
# #     if isValid:
# #         print('Valid \n')
# #     else:
# #         print('Inavlid \n')

# #     productCode = input('Enter a valid product code (type "x" to end) \n')

# # print('Bye!')

# ##########################################################################

# # #\w - any alphanumerical char 

# # wood = 'wood How much wood would a woodchuck chuck if a woodchuck- could chuck wood?'
# # print(re.match(r'wo\w+', wood))
# # print('\n')
# # wood = 'How much wood would a woodchuck chuck if a woodchuck- could chuck wood?'
# # print(re.search(r'wo\w+', wood))

# # print('\n')
# # values = re.findall(r'wo\w+', wood)
# # print(values)

# # print(wood[0:4])
# ##########################################################################


# # wood = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?' 
# # newString = re.sub(r'[aeiou]+', '', wood)  # substitute with an empty string
# # #output
# # print(newString)
# # 'Hw mch wd wld  wdchck chck f  wdchck cld chck wd?' 

# # # 3 args: regex, replacer string, target string
# # newString = re.sub(r'[aeiou]', '*', wood) #removing the plus matches a char at a time. e.g. wood = w**d rather than w*d   
# # #output
# # print(newString)
# # 'H-w m-ch w-d w-ld - w-dch-ck ch-ck -f - w-dch-ck c-ld ch-ck w-d?' 

# ##########################################################################


# # # any name between 1-10 characters long, upper or lower

# # while True:
# #     name = input("Enter your name: ")
# #     valid = re.match('^[a-zA-Z]{1,10}$', name)
# #     if valid:
# #         print('Match')
# #     else:
# #         print('Invalid')



# ##########################################################################

# # ##4 digit pin 
# # while 1:
# #     pin = input('Enter a pin: ')
# #     valid = re.match('^[0-9]{4}$', pin)
# #     if valid:   
# #         print('Match')
# #     else:
# #         print('Invalid')

# ##########################################################################


# finalPin = ''

# while 1:
#     count = 1
#     while count != 5:
#         pin = input(f'Enter pin number {count}: ')
#         valid = re.match('^[0-9]{1}$', pin)
#         if valid:   
#             print('Match')
#             finalPin += pin
#             count += 1
#         else:
#             print('Invalid')

#     print(f'your pin is: {finalPin}')



# ##########################################################################