rows = int(input("Enter how many rows you want to create a mirrored right-angle triangle:"))
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

n = int(input("Now enter the number of rows to create a regular traingle"))

for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()

print("Now let's combine it!")
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()