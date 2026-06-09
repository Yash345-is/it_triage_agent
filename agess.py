secret_number = 27
tries=0
guess = int(input("Try to guess my number!: "))
while guess != secret_number:
    tries=tries+1
    if guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    guess = int(input("Guess again!: "))
    if guess==secret_number:
        tries=tries+1
print("Correct guess! Congratulations!You took",tries," tries to find my number")