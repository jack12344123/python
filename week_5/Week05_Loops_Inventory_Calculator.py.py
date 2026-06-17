items = int(input("how many items: "))
if items >= 100:
    print("to many items")
genale_totle = 0
for i in range(items):
    items_name = input("items_name")
    items_price = float(input("items_price"))
    items_quantity = int(input("inmes_quantity"))

    item_totle = items_price * items_quantity
    genale_totle = genale_totle + item_totle

genale_totle = genale_totle * 1.15
print(genale_totle)



