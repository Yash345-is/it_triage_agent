items = int(input("How may items do you want to purchase?:"))
total = 0
for i in range(items):
    item = input("Enter your item:")
    cost = float(input("Enter the cost price:"))
    total = total + cost
       
print("Total:",total)
payment = float(input(f"Please pay {total} dollars for your items:"))
while payment < total:       
        dueamount = round(total - payment, 2)

        payment += float(input(f"Please pay your pending amount of {dueamount} dollars:"))
if payment > total:
        change = round(payment - total, 2)
        print(f"Here is your change of {change} dollars!")
if payment == total:
        print("Thank you for shopping with us!")
