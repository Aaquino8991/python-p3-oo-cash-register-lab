#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.prev_transactions = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.prev_transactions.append({
            'title': title,
            'price': price,
            'quantity': quantity}
        )

    def apply_discount(self):
        if self.discount > 0:
            self.total -= (self.total * self.discount) / 100
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.prev_transactions:
            return "No previous transactions"
        self.total -= (
            self.prev_transactions[-1]['price'] * self.prev_transactions[-1]['quantity']
        )
        for _ in range(self.prev_transactions[-1]['quantity']):
            self.items.pop()
        self.prev_transactions.pop()