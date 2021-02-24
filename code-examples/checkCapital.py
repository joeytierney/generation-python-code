##Write a program that takes a string, and then returns if the first letter is upper or lowercase? 

myString = input("Enter your String: ")

print("Your String: " + myString)

if myString[0].isupper():
	print("Your String starts with an uppercase")
elif myString[0].islower():
	print("Your String starts with a lowercase")
else:
	print("Your String does not start with a letter")