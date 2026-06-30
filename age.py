try:
    age = int(input("Enter your age:"))
    if age % 2 == 0:
        print("Even age") 
    if age % 2 != 0:
        print("Odd age")


except ValueError as e:
    print(e)

except IOError as f:
    print(f)

except SyntaxError as ea:
    print(ea)

except:
    print("Exception occured")


finally:
    print("This is the end")