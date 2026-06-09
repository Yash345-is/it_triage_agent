password=input("Enter a password:")
length=len(password)

while length<1:
    print("You must enter a password")
    password=input("Enter a password:")
    length=len(password)

print("Your password has",length,"characters")

if length<7:
    print("Weak password")

elif length>=7 and length<11:
    print("Meduim password")

else:
    print("Strong password")
