# Write a function to simulate a number guessing game. 
# Generate a random number and keep checking it against the user's guess. 
# Repeat the loop until they get it right. 
# Display how many attempts it took. 
# 05/01/2021
# joey tierney

import random

num = random.randint(1, 10)

def randomNum(userGuess, userAttempts):
	while num != "guess":
		print("Hard luck! Try again!")
		userGuess = input("Please enter your guess again: ")
		userGuess = int(userGuess)

		userAttempts = userAttempts + 1

		if userGuess == num:
			userAttempts = str(userAttempts)
			print("Congratulations! It took you " + userAttempts + " attempts!")
			break

guess = int(input("Please enter your guess (1 - 10): "))
attempts = 0
randomNum(guess, attempts)