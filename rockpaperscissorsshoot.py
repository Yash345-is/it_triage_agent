import random

choices = ["ROCK","PAPER","SCISSORS"]

computer = random.choice(choices)

you = input("Rock,paper or scissors?:").strip().upper()

print(f"You entered {you} and the computer entered {computer}. Thus:")

if you == computer:
    print("It's a tie!")

elif you == "ROCK":
    if computer == "SCISSORS":
        print("You win!")
    elif computer == "PAPER":
        print("You lose!")

elif you == "PAPER":
    if computer == "SCISSORS":
        print("You lose!")
    elif computer == "ROCK":
        print("You win!")

elif you == "SCISSORS":
    if computer == "ROCK":
        print("You lose!")
    elif computer == "PAPER":
        print("You win!")

