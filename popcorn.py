age = int(input("Enter your age:"))

if age <=12:
    ticket_price=5
    print("Ticket price for kids:$",ticket_price)

if age > 12 and age <=17:
    ticket_price = 8
    print("Ticket price for teenagers:$",ticket_price)

if age >17 and age <=59 :
    ticket_price=12
    print("Ticket price for adults:$",ticket_price)

if age >=60:
    ticket_price=7
    print("Ticket price for seniors:$",ticket_price)

popcorn = input("Do you want popcorn?(Y/N):").strip().lower()

if popcorn == "y":
    ticket_price = ticket_price + 5
    print("New total:$",ticket_price,"\nEnjoy your movie!")

else:
    print("Enjoy your movie!")



