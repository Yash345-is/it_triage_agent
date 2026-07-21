items = ["glue","eraser","sharpener","correction tape","pencil","pen"]

stock_count = [12,0,6,21,0,14]

inventory = {item:count for item, count in zip(items,stock_count) }

print("Full inventory:",inventory)

in_stock_items = [item for item in items if inventory[item]>0]

print("The items in stock are",in_stock_items)

chosen_item = input("Which item do you want to buy?")

if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(chosen_item,"is out of stock.Exitting the checker...")
    exit()

prices = [12,32,21,42,12,8]

print(prices)

increase = int(input("Enter a number to increase all the prices"))

inc = list(map(lambda p:p+increase,prices))

print(inc)