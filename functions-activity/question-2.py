# Write your own username generator, display the persons username.
# Check that the information they have passed through is valid
# and not an empty string as part of the function.
# 05/01/2021
# joey tierney

def generateUser(name, birthYear, favColour):
	username = name[:3] + birthYear[-2:] + favColour[-2:]

	if not name or not birthYear or not favColour:
		print("Invalid input")
	else:
		pass

	return username

for x in range(1):
	name = input("Please enter your Name: ")
	birthYear = input("Please enter your Year of Birth: ")
	favColour = input("Please enter your favourite colour: ")
	username = generateUser(name, birthYear, favColour)
	print("Username:",username,"\n")