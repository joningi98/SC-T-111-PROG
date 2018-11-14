import random

user_choice = input("Rock, Paper or Scissors? ")

r_p_s = ["Rock", "Paper", "Scissors"]

random.shuffle(r_p_s)

computer_choice = r_p_s[0]

print(computer_choice)

if user_choice == "Rock" and computer_choice == 'Paper':
    print("Computer wins!")
if user_choice == "Rock" and computer_choice == 'Scissors':
    print("You win!")
if user_choice == computer_choice:
    print("Draw!")
if user_choice == "Paper" and computer_choice == 'Rock':
    print("You win!")
if user_choice == "Paper" and computer_choice == 'Scissors':
    print("Computer wins!")
if user_choice == "Scissors" and computer_choice == "Rock":
    print("Computer wins!")
if user_choice == "Scissors" and computer_choice == "Paper":
    print("You win!")

