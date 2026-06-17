# Function to add items and their prices
def add_items():
    answer = "yes"  # Start by assuming the user wants to add items

    # Loop runs while the user keeps saying "yes"
    while answer == "yes":
        # Ask user for item name
        item = input("Please enter your item: ")

        # Ask user for item price and convert it to an integer
        price = int(input("Please enter your price: "))

        # Ask if they want to add another item
        answer = input("Add another item? (yes/no): ")

    # This part runs AFTER the loop ends
    # (so answer will usually be "no" here)
    if answer == "yes":
        print("continue")
    else:
        print("No more items added.")


# Call the function to run the program
add_items()




