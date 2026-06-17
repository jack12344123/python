counter = 0

def add_requisition():
    global counter

    print("Enter your information:")
    date = input("Date: ")
    staff_id = input("Stuff ID: ")
    staff_name = input("Stuff Name: ")
    counter += 1
    requisition_id = counter + 10000
    items = []
    total = 0
    print("\nAdd items:")
    answer = "yes"

    while answer == "yes":
        item_name = input("Item Name: ")
        item_price = float(input("Item Price ($): "))
        items.append((item_name, item_price))
        total += item_price
        answer = input("Add another item (yes/no): ").lower()

    return date, staff_id, staff_name, requisition_id, items, total