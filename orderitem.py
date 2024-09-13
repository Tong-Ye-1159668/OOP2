from product import Product

class OrderItem:
    def __init__(self, product, quantity):
        self._product = product
        self._quantity = quantity

    # Getter and setter for product
    def get_product(self):
        return self._product

    def set_product(self, product):
        self._product = product

    # Getter and setter for quantity
    def get_quantity(self):
        return self._quantity

    def set_quantity(self, quantity):
        self._quantity = quantity

    # Calculate total price for the order item
    def get_total_price(self):
        return self._product.productPrice * self._quantity

    # String representation of the OrderItem
    def __str__(self):
        return f"OrderItem(product={self._product.productName}, quantity={self._quantity}, total_price={self.get_total_price()})"
