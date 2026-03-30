item_name = input("Enter item name: ")
item_cost = int(input("Enter item cost: "))
quantity = int(input("Enter quantity: "))

total_cost = item_cost * quantity
remaining_cost = quantity - total_cost
total_cost += (15/100)
print("Total cost: ", total_cost)