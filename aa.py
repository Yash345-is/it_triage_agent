username=input("Enter your username:")
password=input("Enter your password:")

while password=="":
    print("You must enter your password")
    password=input("Enter your password:")

while username=="":
    print("You must enter your username")
    username=input("Enter your username:")

while username==""and password=="":
    print("You must enter your username and password")
    username=input("Enter your username:")
    password=input("Enter your password:")

print("Verfification succesful!")

new_password=input("Enter your new password:")
confirm_password=input("Confirm your new password:")

while new_password!=confirm_password:
    print("Your new password must be the same as your confirmed password!")
    new_password=input("Enter your new password:")
    confirm_password=input("Confirm your new password:")

print("Password change complete!Your password has now changed from",password,"to",new_password)