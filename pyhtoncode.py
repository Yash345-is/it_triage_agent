def add(n1,n2):
    total = n1+n2
    return total

def subtract(n1,n2):
    total = n1-n2
    return total


def multiply(n1,n2):
    total = n1*n2
    return total

def divide(n1,n2):
    total = n1/n2
    return total

choice = int(input("Enter a choice;\n1 for addition,\n2 for subtraction,\n3 for mulitiplication\n4 for division:\n"))
n1 = int(input("Enter number 1:"))
n2 = int(input("Enter number 2:"))

if choice ==  1:
    print(add(n1,n2))

elif choice == 2:
    print(subtract(n1,n2))

elif choice == 3:
    print(multiply(n1,n2))

elif choice == 4:
    print(divide(n1,n2))

else:
    print("Invalid choice")


