balance = 1000
while True:
    print("Option 1. Check Balance")
    print("Option 2. Deposit Money")
    print("Option 3. Withdraw Money")
    print("Option 4. Exit")
    choice = input("Choose an option: ")
    
    if choice =="2":
        deposit=int(input("How much money would you like to deposit into your bank account?")) 
        print("Transaction succesful!")
        balance=balance+deposit
        
    elif choice =="3":
        withdraw = int(input("How much money would you like to withdraw from your bank account? "))

        while withdraw > balance:
            print("Error! Not enough money for withdrawal")
            withdraw = int(input("How much money would you like to withdraw from your bank account?: "))

        balance = balance - withdraw
        print("Withdrawal successful!")
        
    elif choice=="4":
        print("Thank you for using the Automated Teller Machine!")
        break
    print("You now have",balance,"in your bank account!")