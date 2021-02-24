# #challenge task - Write an algorithm that takes any string length and tries to access what is at 
# index position 10. If the string length is less than 10 it will throw an error. 
# Test multiple string lengths. 

validLength = False

while not validLength:
    userString = input("Please enter a String: ")

    if len(userString) < 10:
        try:
            print("\nIndex position 10 of your string is: " + userString[10])
            validLength = True
        except:
            print("String is less than 10! Try again!")
    else:
        print("\nIndex position 10 of your string is: " + userString[10])
        validLength = True

#########

# # challenge task - Write an algortitm that declares two numbers, where one of them is 0. 
# Try and multiply the two numbers. In python any integer / 0 will throw an error. 

num1 = 0
num2 = int(input("Please enter a number: "))

try:
    numsSum = (num2 / num1)
    print(numsSum)
except:
    print("Error: Cannot divide by 0")


#########

# # # challenge task - Write an algorithm that asks the users to input an integer. 
# # Handle a situation where the user does not enter an integer and an error would be thrown. 

validNum = False

while not validNum:
    
    try:
        userNum = int(input("Please enter a number: "))
        print("\nThe number you entered is:",userNum)
        validNum = True
    except:
        print("***** Sorry, that is not a number, try again! *****\n")
        



# import winsound
# frequency = 2500  # Set Frequency To 2500 Hertz
# duration = 1000  # Set Duration To 1000 ms == 1 second

# winsound.Beep(frequency, duration)


# try - this is the block to be attempted 
# except - will execute if there is an error in the try block
# finally - will always be executed 
# else - will be run if there is not error in the try block


####################################################################################



# def add(n1,n2):
#     print(n1+n2)

# add(10,20)
# #This will provide an error 
# number1 = 10
# number2 = input("Please provide a number")
# # add(number1, number2)


####################################################################################

# def add(n1,n2):
#     sum = n1+n2
#     return sum

# try:
#     #want to attempt this code
#     number1 = 10
#     number2 = int(input("Please provide a number: "))
# except:
#     #what happens if there is an error 
#     print("This is the except handler, your try statement did not work.")
# else:
#     #runs if there is not an error
#     sumOut = add(number1, number2)
#     print("If there is no error, this will run in addition to the try")
#     print(sumOut)



####################################################################################


# ##will try and open a file called text.txt in write mode. If it does not exist it will create a new one. 
# try: 
#     f = open('text.txt', 'w')
#     f.write(90)
# except TypeError:
#     print("Type Error")
# except OSError:
#     print("OS error")
# except:
#     print("All other exeptions")
# finally:#optional
#     print("I always run")


####################################################################################


# def askForInt():
#     while True:
#         try:
#             result = int(input("Please provide a number: "))
#         except:
#             print("Whoops, this is not a number")
#             break
#         else:
#             print("Yes, thank you")
#             break
#         finally:
#             print("I am going to ask you again")
            
#     print('Function done \n')        

# while(1):
#     askForInt()
#     print('Break statement worked, keep going')