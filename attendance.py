medical_leave=input("Have you missed classes because of MC?(Y/N):").strip().upper()
dice=input("Do you want to roll the dice?(Y/N):").strip().upper()
if medical_leave=="Y":
    print("You are allowed for the exam")
if medical_leave=="N":
    attendance=float(input("Enter your attendance percentage"))
    if attendance>=75:
        print("You are qualified to take the exam")
    else:
        print("You are not qualified to take the exam")