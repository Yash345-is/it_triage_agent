number = int(input("Enter a number: "))
count = 0
for digit in str(number):
    count += 1
print("You have",count,"digits in your number")
