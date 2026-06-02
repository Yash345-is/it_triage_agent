age = int(input("Enter your age: "))

codes = {
    10: ("102016", "You get a 30% discount on Robux!"),
    11: ("112015", "You get a free 1 month YouTube Premium subscription!"),
    12: ("122014", "You get a new iPhone 17 Pro Max!"),
    13: ("132013", "You get a free pair of AirPods!"),
    14: ("142012", "You get a free 1 month Spotify Premium subscription!"),
    15: ("152011", "You get a free 1 month YouTube Premium subscription!"),
    16: ("162010", "You get $3,500!"),
    17: ("172009", "You get a free scholarship to any college you want!"),
    18: ("182008", "You get a free $3750 voucher for anything you want!"),
    19: ("192007", "You get the brand new S26 Ultra!"),
    20: ("202006", "You get a new Tesla Model Y!")
}

if age not in codes:
    print("You will be redirected to another page")

else:
    print("You will be given a verification code to put in later")

    code, reward = codes[age]

    print("Your verification code is", code)

    verification = input("Enter your verification code: ")

    if verification == code:
        print(reward)
    else:
        print("Invalid code! Try again.")