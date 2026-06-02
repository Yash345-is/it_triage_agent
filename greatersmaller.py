marks=int(input("Enter your marks"))
if marks>70:
    print("The grade is A")
elif marks>65 and marks<=70:
    print("The grade is B")
elif marks>60 and marks<=65:
    print("The grade is C")
elif marks>50 and marks<=60:
    print("The grade is D")
else:
    print("The grade is F")