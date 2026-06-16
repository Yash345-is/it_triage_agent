def total_calc(bill_amount,tip_perc):
    total_amount = bill_amount*(1+ 0.01 * tip_perc)

    print(f"Please pay ${total_amount}")

total_calc(150,20)