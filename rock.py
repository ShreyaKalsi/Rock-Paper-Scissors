import random

from sqlalchemy import true

choices = ['rock', 'paper', 'scissors']

def get_user_choice():
    user_input = input("Enter rock, paper, or scissors: ").lower()
    while user_input not in choices:
        user_input = input("Invalid choice. Enter rock, paper, or scissors: ").lower()
    return user_input

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win"
    else:
        return "Computer wins"

def main():
    while true:
        play_again = input("Do you want to play Rock, Paper, Scissors? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    main()