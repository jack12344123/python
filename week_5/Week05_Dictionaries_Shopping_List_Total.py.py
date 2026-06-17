shopping_list = {}
total = 0
while True:
    item_name = input("Enter item name: ")
    if item_name == 'stop':
        break
    item_price = float(input("Enter item price: "))
    if item_price == 'stop':
        break
    shopping_list[item_name] = item_price
    total += item_price
print(shopping_list)
print("total", total)





