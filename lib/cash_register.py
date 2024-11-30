class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append(title)
        self.total += price * quantity
        self.last_transaction = price * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        if self.items:
            self.items.pop()
        self.last_transaction = 0

    def get_total(self):
        return f"Your total is ${self.total:.2f}"

# If this file is run as a script, execute the following code
if __name__ == "__main__":
    # Create a register with a 20% discount
    register = CashRegister(20)

    # Add some items
    register.add_item("Macbook Air", 1000)
    register.add_item("Phone", 500, 2)

    # Apply the discount
    register.apply_discount()

    # Print the current total
    print(register.get_total())
