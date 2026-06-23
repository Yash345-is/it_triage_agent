try:
    num1, num2 = eval(input("Enter two numbers with a comma in between them:"))
    result = num1/num2
    print(result)

except ValueError as e:
    print(e)

except ZeroDivisionError as f:
    print(f)
except SyntaxError as dea:
    print(dea)
except:
    print("Exception occured")

finally:
    print("This is the end")