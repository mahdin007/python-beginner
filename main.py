#Rock paper siccors game.
import random 

def get_choices(): 
  player_choice = input("Enter your Choise (Rock, Paper, Scissors: ")
  options = ["Rock", "Paper", "Scissors"]
  computer_choice = random.choice(options)
  choices = {"Player" : player_choice, "Computer" : computer_choice} 
  return choices

choices = get_choices()
print(choices)
