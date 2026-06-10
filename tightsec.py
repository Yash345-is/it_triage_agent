correctpassword=76892543

verifier=input("Enter your password:")




while verifier!=correctpassword:
    print("Invalid password")
    verifier=input("Enter the correct password:")
    if verifier==correctpassword:
        print("Access granted")

