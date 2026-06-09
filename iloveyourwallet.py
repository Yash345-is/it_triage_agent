item=input("Enter your first item:")
price=float(input("Enter the price of your first item:"))
item2=input("Enter your second item:")
price2=float(input("Enter the price of your second item:"))
item3=input("Enter your third item:")
price3=float(input("Enter the price of your third item:"))
total=price+price2+price3
gst=total*0.09
final_total=total+gst
print("\n----RECEIPT----\nItem:", item, "\nPrice:", price,"\nItem:",item2,"\nPrice:",price2,"\nItem:",item3,"\nPrice:",price3,"\nSubtotal:",total,"\nGST:",gst,"\nFinal total:",final_total,"\n----RECIEPT----")

