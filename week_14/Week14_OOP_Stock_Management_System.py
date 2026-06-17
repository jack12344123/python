class StockInfo:
    def __init__(self, product_name, product_price, stock_quantity, product_id):
        self.product_name = product_name
        self.product_price = product_price
        self.stock_quantity = stock_quantity
        self.product_id = product_id


class StockManagement:
    def __init__(self):
        self.product_list = []
        self.sales_list = []

    def add_product(self):
        product_name = input("Enter product name: ")
        product_id = input("Enter product ID: ")

        for product in self.product_list:
            if product.product_id == product_id:
                print("Product ID already exists.")
                return

        product_price = float(input("Enter product price: $"))
        stock_quantity = int(input("Enter stock quantity: "))

        new_product = StockInfo(product_name, product_price, stock_quantity, product_id)
        self.product_list.append(new_product)

        print("Product added successfully!")

    def view_all_products(self):
        if len(self.product_list) == 0:
            print("No products found.")
            return

        for product in self.product_list:
            print("----------------")
            print("Product ID:", product.product_id)
            print("Product Name:", product.product_name)
            print("Product Price: $", product.product_price)
            print("Stock Quantity:", product.stock_quantity)

    def update_stock(self):
        product_id = input("Enter product ID: ")

        for product in self.product_list:
            if product.product_id == product_id:
                amount = int(input("Enter amount to add: "))
                product.stock_quantity += amount
                print("Stock updated successfully!")
                return

        print("Product not found.")

    def sell_product(self):
        product_id = input("Enter product ID: ")

        for product in self.product_list:
            if product.product_id == product_id:
                quantity_sold = int(input("Enter quantity sold: "))

                if quantity_sold > product.stock_quantity:
                    print("Not enough stock.")
                    return

                product.stock_quantity -= quantity_sold
                total_price = quantity_sold * product.product_price

                sale = {
                    "product_id": product.product_id,
                    "quantity_sold": quantity_sold,
                    "total_price": total_price
                }

                self.sales_list.append(sale)

                print("Sale completed successfully!")
                print("Total price: $", total_price)
                return

        print("Product not found.")

    def search_product(self):
        product_id = input("Enter product ID: ")

        for product in self.product_list:
            if product.product_id == product_id:
                print("Product ID:", product.product_id)
                print("Product Name:", product.product_name)
                print("Product Price: $", product.product_price)
                print("Stock Quantity:", product.stock_quantity)
                return

        print("Product not found.")

    def display_summary(self):
        total_products = len(self.product_list)
        total_items_sold = 0
        total_sales_value = 0

        for sale in self.sales_list:
            total_items_sold += sale["quantity_sold"]
            total_sales_value += sale["total_price"]

        print("Total number of products:", total_products)
        print("Total items sold:", total_items_sold)
        print("Total sales value: $", total_sales_value)

        print("Current stock levels:")
        for product in self.product_list:
            print(product.product_name, ":", product.stock_quantity)

    def menu(self):
        while True:
            print("\n--- Stock Management Menu ---")
            print("1. Add Product")
            print("2. View All Products")
            print("3. Update Stock")
            print("4. Sell Product")
            print("5. Search Product")
            print("6. View Sales Summary")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.view_all_products()
            elif choice == "3":
                self.update_stock()
            elif choice == "4":
                self.sell_product()
            elif choice == "5":
                self.search_product()
            elif choice == "6":
                self.display_summary()
            elif choice == "7":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")


stock = StockManagement()
stock.menu()


