#A bunch of code that messes around with String Manipulation
#04/01/2021
#joey tierney

myString = "Hello World"

print("\nOriginal String: " + myString + "\n")

cFold = myString.casefold()

print("New String (casefold): " + cFold)

print("\nString centered:\n" + myString.center(20))

findWord = myString.find("World")

print("\n" + "Word 'World' number of characters into the String:",findWord)

alpha = myString.isalpha()

print("\nAre the characters in the String all in the alphabet:",alpha)