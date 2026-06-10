secret_number=27

tries=5

guess=int(input("Try to guess my number!:"))

if guess!=secret_number:
    tries=tries-1
    print("Tries left:",tries)
    

while guess!=secret_number:
    tries-=1
    if guess>secret_number:
        guess=int(input("Too high!Guess again:"))
        print("Tries left:",tries)

    if guess<secret_number:
        guess=int(input("Too low!Guess again:"))
        print("Tries left:",tries)

    if tries==0:
        print("Game over!The secret number was",secret_number)
        break

else:
    print("Congratualtions!You guessed the number with",tries,"tries left!")
    


