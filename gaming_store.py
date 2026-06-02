print("Yashas's gaming store!Gaming devices,video game controllers,anything;you name it!")
gaming_store=float(input("How much money have you spent on Yashas's gaming store?"))
if gaming_store<1000:
    print("You're not really a buyer,so you'll get a 2.5% discount on your next purchase.")
if gaming_store>1000 and gaming_store<3000:
    print("You're an uncommon customer.So its going to be a 15% discount for you,my friend.")
if gaming_store>5000 and gaming_store<7500:
    print("Familiar face.You get a 25% discount.")
if gaming_store>7500 and gaming_store<10000:
    print("Thanks for the amount you've spent on our store!In return,you will be receiving a 45% discount on your next purchase!")
if gaming_store>10000:
    print("Don't be shocked when you see your next item at 1/4 of the price it used to be.75% discount for you!")