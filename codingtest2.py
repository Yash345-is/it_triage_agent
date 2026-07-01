try:
    n1 = float(input("Enter a number:"))
    n2 = float(input("Enter a number:"))
    choice = int(input("There are four choices.1,2,3 and 4.Using the 2 inputted above,enter 1 to add the two numbers\nenter 2 the subtract the two numbers\nenter 3 to mulitply the numbers\nenter 4 to divide the numbers:"))
    def MyAdd(n1,n2):
            total = n1 + n2
            return total
    def MySubtract(n1,n2):
            subtract = n1 - n2
            return subtract
    def MyMultiply(n1,n2):
            multiply = n1 * n2
            return multiply
    def MyDivide(n1,n2):
            divide = n1 / n2
            return divide
    if choice == 1:
        print(MyAdd(n1,n2))

    elif choice == 2:
        print(MySubtract(n1,n2))
            
    elif choice == 3:
        print(MyMultiply(n1,n2))
        
    elif choice == 4:
        print(MyDivide(n1,n2))
        
            
    
except ValueError as e:
    print(e)

except ZeroDivisionError as f:
    print(f)

except:
    print("Exception occured")

finally:
    print("This is the end")
