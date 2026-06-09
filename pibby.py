totalsaved=0

goal=float(input("Enter your goal of how much money you want to save:"))
reach=goal
saving=float(input("How much money do you want to keep in your piggy bank?:"))

while totalsaved<goal:
    totalsaved=totalsaved+saving
    reach=goal-totalsaved
    saving=float(input("How much money do you want to keep in your piggy bank?:"))
    print("Total saved:",totalsaved,"\nAmount kept:",saving,"\nMoney left to save:",reach)

print("Goal of",goal,"saved!Congratulations")
