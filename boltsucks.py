import random
print("Race 1 of formula brawl!")
print("The racers of this 3 race series are:\nMeeple\nShelly\nLeon\nBolt\nColt\nSpike")

Racers=["Bolt","Shelly","Spike","Colt","Meeple","Leon"]


win1 = random.choice(Racers)


win2 = random.choice(Racers)
while win2 == win1:
    win2 = random.choice(Racers)


win3 = random.choice(Racers)
while win3 == win1 or win3 == win2:
    win3 = random.choice(Racers)


win4 = random.choice(Racers)
while win4 == win1 or win4 == win2 or win4 == win3:
    win4 = random.choice(Racers)


win5 = random.choice(Racers)
while win5 == win1 or win5 == win2 or win5 == win3 or win5 == win4:
    win5 = random.choice(Racers)

win6 = random.choice(Racers)
while win6 == win1 or win6 == win2 or win6 == win3 or win6 == win4 or win6 == win5:
    win6 = random.choice(Racers)
results = [win1, win2, win3, win4, win5, win6]
guess=input("Which brawler do you think will win the first race?:")

print("🏁 FINAL RACE RESULTS 🏁")
print("🥇 1st:", win1)
print("🥈 2nd:", win2)
print("🥉 3rd:", win3)
print("4th:", win4)
print("5th:", win5)
print("6th:", win6)
print("Your prediction:",guess,"\nFinal position:",results.index(guess)+1)

print("Race 2 of formula brawl!")

Racers=["Bolt","Shelly","Spike","Colt","Meeple","Leon"]


win1 = random.choice(Racers)


win2 = random.choice(Racers)
while win2 == win1:
    win2 = random.choice(Racers)


win3 = random.choice(Racers)
while win3 == win1 or win3 == win2:
    win3 = random.choice(Racers)


win4 = random.choice(Racers)
while win4 == win1 or win4 == win2 or win4 == win3:
    win4 = random.choice(Racers)


win5 = random.choice(Racers)
while win5 == win1 or win5 == win2 or win5 == win3 or win5 == win4:
    win5 = random.choice(Racers)

win6 = random.choice(Racers)
while win6 == win1 or win6 == win2 or win6 == win3 or win6 == win4 or win6 == win5:
    win6 = random.choice(Racers)
results = [win1, win2, win3, win4, win5, win6]
guess=input("Which brawler do you think will win the second race?:")

print("🏁 FINAL RACE RESULTS 🏁")
print("🥇 1st:", win1)
print("🥈 2nd:", win2)
print("🥉 3rd:", win3)
print("4th:", win4)
print("5th:", win5)
print("6th:", win6)
print("Your prediction:",guess,"\nFinal position:",results.index(guess)+1)






print("Race 3 of formula brawl!")


Racers=["Bolt","Shelly","Spike","Colt","Meeple","Leon"]


win1 = random.choice(Racers)


win2 = random.choice(Racers)
while win2 == win1:
    win2 = random.choice(Racers)


win3 = random.choice(Racers)
while win3 == win1 or win3 == win2:
    win3 = random.choice(Racers)


win4 = random.choice(Racers)
while win4 == win1 or win4 == win2 or win4 == win3:
    win4 = random.choice(Racers)


win5 = random.choice(Racers)
while win5 == win1 or win5 == win2 or win5 == win3 or win5 == win4:
    win5 = random.choice(Racers)

win6 = random.choice(Racers)
while win6 == win1 or win6 == win2 or win6 == win3 or win6 == win4 or win6 == win5:
    win6 = random.choice(Racers)
results = [win1, win2, win3, win4, win5, win6]
guess=input("Which brawler do you think will win the third race?:")

print("🏁 FINAL RACE RESULTS 🏁")
print("🥇 1st:", win1)
print("🥈 2nd:", win2)
print("🥉 3rd:", win3)
print("4th:", win4)
print("5th:", win5)
print("6th:", win6)
print("Your prediction:",guess,"\nFinal position:",results.index(guess)+1)

print("Thank you for participating in formula brawl!We hope you enjoyed seeing our contestants race and opening your rewards!")