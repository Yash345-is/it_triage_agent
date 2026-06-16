import random
magicbox=input("Do you want to open the magic box? Either gain,loss or nothing changes?(Y/N):").strip().upper()
if magicbox == "Y":
    print("The magic box is opening....")
    reward = random.randint(1,6)
    if reward == 1:
        print("💀You get nothing!💀")
    if reward == 2:
        print("🍬You get candy!🍬")
    if reward == 3:
        print("😭Your wallet will be crying😭.You lose 50% of your wealth!")
    if reward == 4:
        print("Congrats!You got the best power of all,super speed!")
    if reward == 5:
        print("Your day is made!You get $200!💸💸💸")
    if reward == 6:
        print("Bad luck!You fall down in public!😒")

if magicbox == "N":
    reward=random.randint(1,6)
    if reward == 1:
        print("You would've got nothing if you agreed.You don't need to feel bad")
    if reward == 2:
        print("You missed out on free candy!")
    if reward == 3:
        print("You were REALLY lucky you didn't want to play.If you did,half of your wallet would vanish in an instant")
    if reward == 4:
        print("You're gonna punch the wall.You could've got super speed!")
    if reward == 5:
        print("Your day would've been made!You would've gotten $200!💸💸💸")
    if reward == 6:
        print("If you said yes to the magic box,all your integrity would be gone " \
        "because you would've fell down in public.That was a narrow escape,my friend!")
