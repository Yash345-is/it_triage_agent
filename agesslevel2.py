import random

print("Choose difficulty:")
print("1. Easy (1 to 10, 5 tries)")
print("2. Medium (1 to 50, 7 tries)")
print("3. Hard (1 to 100, 10 tries)")

choice = input("Enter 1, 2 or 3: ")

if choice == "1":
    secret_number = random.randint(1, 10)
    tries = 5

elif choice == "2":
    secret_number = random.randint(1, 50)
    tries = 7

else:
    secret_number = random.randint(1, 100)
    tries = 10


guess = int(input("Try to guess the number: "))

while guess != secret_number and tries > 1:
    tries -= 1

    if guess > secret_number:
        print("Too high!")
    else:
        print("Too low!")

    print("Tries left:", tries)
    guess = int(input("Guess again: "))

if guess == secret_number:
    print("Correct! You win!")
else:
    print("Game Over! The number was", secret_number)