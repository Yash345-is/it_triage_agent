def cube(num):
    
    return num ** 3

num = int(input("Enter a number:"))

if num % 3 == 0:
    print(cube(num))

else:
    print("Not divisible!")