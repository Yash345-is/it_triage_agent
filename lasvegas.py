number = 7

guess = int(input("Guess the number from 1 to 10: "))

while guess != number:
    print("Wrong number!")
    guess = int(input("Guess again: "))

print("Congratulations! You guessed the number!")
