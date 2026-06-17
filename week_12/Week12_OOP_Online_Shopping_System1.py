class Online_shopping:
    def __init__(self, customer_name, product_name, price, quantity):
        self.customer_name = customer_name
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def calculate_cost(self):
        total = self.price * self.quantity
        return total

    def discount(self):
        total = self.calculate_cost()
        if total >= 500:
            discount_total = total - (total * 0.3)
            return discount_total

        else:
            return  total
    def cart(self):
        print("customer_name ", self.customer_name)
        print("product_name ", self.product_name)
        print("price ", self.price)
        print("quantity ", self.quantity)
        print("discount ", self.discount())
        print("total ", self.calculate_cost())

cart1 = Online_shopping("jack", "laptop", 1000, 2)
cart2 = Online_shopping("tim", "food", 10, 3)

cart1.calculate_cost()
cart1.discount()
cart1.cart()



cart2.calculate_cost()
cart2.discount()
cart2.cart()











