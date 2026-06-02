secret_number = 27
guess = int(input("Try to guess my number!: "))
while guess != secret_number:
    if guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    guess = int(input("Guess again!: "))
print("Correct guess! Congratulations!")