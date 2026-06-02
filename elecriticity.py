print("Mothly Electricity Tax")
units=int(input("Enter the amount of electritcity units you have used this month"))
if units<50:
    original_bill=2.60*units
    tax_bill=25
elif units>=50 and units<100:
    original_bill=3.25*units
    tax_bill=35
elif units>=100 and units<200:
    original_bill=5.26*units
    tax_bill=45
elif units>=200:
    original_bill=8.45*units
    tax_bill=75
sum=original_bill+tax_bill
print("Your electricity bill for this month will be",sum,"dollars")