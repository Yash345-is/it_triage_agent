import random
dice=input("Do you want to roll the dice?(Y/N):").strip().upper()

while dice == "Y":
    roll= random.randint(1,6)
    print("The dice landed on",roll)

    dice = input("Do you want to roll again? (Y/N): ").strip().upper()

print("Thanks for playing!")
    
    





