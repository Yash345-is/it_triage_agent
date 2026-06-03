num=int(input("Enter a number"))
while num==float:
    input("Enter a WHOLE number")

digit=float(input("Enter a decimal digit,or add more if you want"))
while digit==int:
    input("Enter a number with DECIMALS")

num_digit=num+digit
while digit >= 1.0:
    digit = float(input("Enter a decimal digit LESSER than 1.0: "))

num_digit=num+digit
print("This is",num_digit, "before rounding off to the nearest number")

    
if digit<0.5:
    num_digit=num
    print("This is",num_digit,"after rounding off to the nearest number")
if digit>=0.5:
    num_digit=num+1
    print("It now becomes",num_digit,"after rounding off to the nearest number")
    