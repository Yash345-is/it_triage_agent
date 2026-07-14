import random

code = random.randint(100,999)
tries = 10

guess = int(input("You have just found a mysterious digital device.The pin is a three digit number.Ten   guesses what it is!:"))

if guess != code:
    tries = tries-1
    print(f"Tries left:{tries}")

while guess != code:
    tries=tries-1
    if abs(guess-code) <= 10:
        print("You're very close!")
        guess = int(input("Guess again!:"))
    elif guess > code:
        print("Too high!")
        guess = int(input("Guess again!:"))
    elif guess < code:
        print("Too low!")
        guess = int(input("Guess again!:"))
    print(f"Tries left:{tries}")
    
    if tries == 0:
        print(f"Game over!The code was {code}!")
        break
if guess == code:
    print("Congratulations!You guessed the code!")

rematch = input("Do you want to play again(Y/N)?:").strip().upper()

while rematch == "Y":
    code = random.randint(100,999)
    tries = 5

    guess = int(input("You have just found a mysterious digital device.The pin is a three digit number.Five guesses what it is!:"))

    if guess != code:
        tries = 4
        print(f"Tries left:{tries}")
    while guess != code:
        tries=tries-1
        
        if guess > code:
            print("Too high!")
            guess = int(input("Guess again!:"))
            if abs(guess-code) <= 10:
                print("You're very close!")
        elif guess < code:
            print("Too low!")
            guess = int(input("Guess again!:"))
            if abs(guess-code) <= 10:
                print("You're very close!")
                guess = int(input("Guess again!:"))
        print(f"Tries left:{tries}")
    
        if tries == 0:
            print(f"Game over!The code was {code}!")
            break

    
    if guess == code:
        print("Congratulations!You guessed the code!")
    rematch = input("Do you want to play again(Y/N)?:").strip().upper()

