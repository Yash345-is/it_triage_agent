deposit = float(input("How much money have you deposited in this bank?:"))
time = int(input("How many months are you planning to keep your money in our bank?:"))
interest = (deposit / 100) * 5 * (time / 12)

print("Interest earned over",time,"months:$",interest)

total = deposit + interest

print("New balance:$",total)
