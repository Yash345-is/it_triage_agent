number = input("Enter a number: ")

if number == "":
    print("You must enter a number")
    number = input("Enter a number: ")

number = int(number)

if number > 0:
    print(number, "is a positive number")

elif number < 0:
    print(number, "is a negative number")

else:
    print("Zero")
