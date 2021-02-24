# rock paper scissors with a semi-working login function
# 06/01/2021
# joey tierney

import random, time

rps = ['rock', 'paper', 'scissors']
username = ['joey', 'patton', 'rommel']
password = ['thenownow', 'longwalks', 'thebigdog']
playerWins = 0
computerWins = 0
rounds = 0

def login():
    user = input("Please enter your username: ")
    passW = input("Please enter your password: ")
    
    if user in username and passW in password:
        print("\n***** Login successful! *****\nLoading game...\n")
        time.sleep(3)
    else:
        print("Incorrect username or password")
        exit() # program ends with invalid username and password combo

def winningConditions(playerChoice, computerChoice):
    if playerChoice == computerChoice:
        return 'draw'
    elif playerChoice == 'rock' and computerChoice == 'scissors':
        return 'player'
    elif playerChoice == 'scissors' and computerChoice == 'paper':
        return 'player'
    elif playerChoice == 'paper' and computerChoice == 'rock':
        return 'player'
    else:
        return 'computer'

def game(playerWins, computerWins):
    for rounds in range(3):
        while playerWins < 2 or computerWins <2:
            print("Round",rounds + 1,"\n")
            print("********** Current score **********")
            print("\nPlayer:",playerWins)
            print("\nComputer:",computerWins,"\n")

            playerChoice = input("Rock, Paper, or Scissors?\nEnter choice: ")
            playerChoice = playerChoice.lower()

            if playerChoice in rps:
                computerChoice = random.choice(rps)
                print("\nComputer's choice is: " + computerChoice)
            
            if playerChoice not in rps:
                print("\nInvalid input! Please enter 'Rock, Paper, or Scissors'\n")
                game(playerWins, computerWins)

            winner = winningConditions(playerChoice, computerChoice)
            if winner == 'player':
                print("\nCongratulations! You win!\n")
                playerWins += 1
                rounds+1
                break
            elif winner == 'computer':
                print("\nOh no! You lost :(\n")
                computerWins += 1
                rounds+1
                break
            elif winner == 'draw':
                print("\nYou drew! Play this round again! :D\n")

        if playerWins == 2:
            print("\nWoohoo! You won the game! :D")
        elif computerWins == 2:
            print("\nWell...better luck next time :/")

login()
game(playerWins, computerWins)