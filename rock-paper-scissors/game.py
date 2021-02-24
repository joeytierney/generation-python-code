import random
print('Welcome, to the king of ROCK fist tournament: Choose between Rock, Paper and Scissors: ')

R_P_S = ['rock', 'paper', 'scissors']
PLAYER_WINS = 0
COMPUTER_WINS = 0

def winning(computer_choice, player_choice):
  if computer_choice == player_choice:
    return 'draw'
  elif computer_choice == 'paper' and player_choice == 'rock':
    return 'computer'
  elif computer_choice == 'rock' and player_choice == 'scissors':
    return 'computer'
  elif computer_choice == 'scissors' and player_choice == 'paper':
    return 'computer'
  else:
    return 'player'

for round in range(3):
  while PLAYER_WINS < 2 or COMPUTER_WINS < 2:
    print('Round', round + 1, ': FIGHT!')
    player_choice = input('Choose your fighter (rock, paper, scissors): ')
    player_choice = player_choice.lower()
    
    print(f'Player = {PLAYER_WINS}     Computer = {COMPUTER_WINS}')
    if player_choice in R_P_S:
      computer_choice = random.choice(R_P_S)
      print(f'[Round {round + 1}]: Computer choice is {computer_choice}')

      winner = winning(computer_choice, player_choice)
      if winner == 'computer':
        print('You Lose!')
        COMPUTER_WINS += 1
      elif winner == 'player':
        print('You Win!')
        PLAYER_WINS += 1
      elif winner == 'draw':
        print("It's a Draw")
    else:
      print('Please choose: ROCK PAPER or SCISSORS!!')

  if PLAYER_WINS == 2:
    print('Player WINS!!')
  elif COMPUTER_WINS == 2:
    print('Computer WINS!!!')

