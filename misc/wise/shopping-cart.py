from collections import defaultdict
from time import process_time_ns


class CartItem:
    def __init__(self, id: str, quantity: int, unit_price: int):
        self.id = id
        self.quantity = quantity
        self.unit_price = unit_price


class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def addItem(self, item: CartItem):
        self.cart[item.id] = item

    def removeItem(self, item: CartItem, quantity: int):
        if item.id not in self.cart:
            raise Exception("Error: Item not in cart")

        if quantity <= 0:
            raise Exception("Error: Quantity cannot be negative")

        self.cart[item.id].quantity = max(0, self.cart[item.id].quantity - quantity)


    def calculateTotal(self):
        total_price = 0
        for cart_item in self.cart.values():
            total_price += cart_item.unit_price * cart_item.quantity
        return total_price


cart = ShoppingCart()
apple = CartItem("apple", 5, 10)
banana = CartItem("banana", 12, 30)
mangoes = CartItem("mangoes", 2, 80)
watermelon = CartItem("watermelon", 1, 25)
cart.addItem(apple)
print(cart.calculateTotal())
cart.addItem(banana)
print(cart.calculateTotal())
cart.addItem(mangoes)
print(cart.calculateTotal())
cart.addItem(watermelon)
print(cart.calculateTotal())
cart.removeItem(mangoes, -60)
print(cart.calculateTotal())
