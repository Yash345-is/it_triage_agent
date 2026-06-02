print("YouTube Premium subscription")

mail = input("Enter your e-mail: ")
password = input("Enter your password: ")

if not mail and not password:
    print("You must enter your e-mail and your password")

elif not mail:
    print("You must enter your e-mail")

elif not password:
    print("You must enter your password")

else:
    answer = input("Do you agree to our terms and conditions? (yes/no): ")

    if answer == "yes" or answer == "Yes":
        print("Thank you for subscribing to YouTube Premium! Enjoy ad-free videos!")
    else:
        print("You must agree to the terms and conditions to subscribe to YouTube Premium")