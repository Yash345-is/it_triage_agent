total = 0
for i in range(5):
    number = float(input("Enter the price of the  item: "))
    total += number 
gst=(total/100)*9
number_gst=total+gst    
print("the total(inclusive of GST)is",number_gst)