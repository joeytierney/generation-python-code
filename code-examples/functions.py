def canCode(i, k):

	ins = input("Do you have Python installed? ")
	know = input("Do you know how to code in Python? ")

	if ins == i and know == k:
		print("You can code! :D")
	else:
		print("Sorry, you cannot code :/")

installed = 'True'
knowledge = 'True'

canCode(installed, knowledge)