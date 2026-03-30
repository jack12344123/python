
def add_items():
    items = {}

    answer = "yes"
    while answer == "yes":
        item_name = input("Please enter your item: ")
        price = int(input("Please enter your price: "))
        items[item_name]= price  # add to dictionary

        answer = input("Add another item? (yes/no): ")
    if answer == "yes":
        print("continue")
    else:
        print("No more items added.")
    for item, price in items.items():
        print(item, price)
add_items()

