monthly_income = int(input("Enter your income: "))
rent = int(input("Enter your rent: "))
transport_cost = int(input("Enter your transportation cost: "))
entertainment_cost = int(input("Enter your entertainment cost: "))
food_cost = int(input("Enter your food cost: "))

total_cost = rent + transport_cost + entertainment_cost +food_cost
remaining_cost = monthly_income - total_cost

print("Total cost: ", total_cost)
print("Remaining cost: ", remaining_cost)
