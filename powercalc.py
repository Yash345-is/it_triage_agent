print("This python designed calculator can calculate the power of 2 numbers!Check for yourself!")
number = int(input("Enter your number: "))
power = int(input("Enter your power: "))
result = 1
for i in range(power):
    result = result * number
print("The power of",number,"to",power,"is",result)