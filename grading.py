marks=int(input("Enter your marks"))
if marks in range(70,100):
    print("The grade is A")
elif marks in range(65,70):
    print("The grade is B")
elif marks in range(60,65):
    print("The grade is C")
elif marks in range(50,60):
    print("The grade is D")
else:
    print("The grade is F")