#Rock paper siccors game.
import random 

def get_choices(): 
  player_choice = input("Enter your Choise (Rock, Paper, Scissors): ")
  options = ["Rock", "Paper", "Scissors"]
  computer_choice = random.choice(options)
  choices = {"Player" : player_choice, "Computer" : computer_choice} 
  return choices

def check_win(player, computer):
  print(f"You chose {player}, Computer chose {computer}") 
  if player == computer:
    return "It's a Tie."
  elif player == "Rock":
    if computer == "Scissors":
      return "Rock smashes! You win!"
    else:
      return "Paper covers! You lose."
  elif player == "Paper":
    if computer == "Rock":
      return "Paper covers! You win!"
    else:
      return "Scissors cuts! You lose."
  elif player == "Scissors":
    if computer == "Paper":
      return "Scissors cuts! You win!"
    else:
      return "Rock smashes! You lose."
      
choices = get_choices()
result = check_win(choices["Player"], choices["Computer"])

print(result) 