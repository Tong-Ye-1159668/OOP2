from datetime import datetime
from orderitem import OrderItem

class Order:
    nextID = 10000

    def __init__(self, customer):
        self._orderID = Order.nextID
        Order.nextID += 1
        self._customer = customer
        self._orderDate = datetime.now()
        self._order_items = []

    # Getter for orderID (ID shouldn't change, so no setter)
    def get_order_id(self):
        return self._orderID

    # Getter and setter for customer
    def get_customer(self):
        return self._customer

    def set_customer(self, customer):
        self._customer = customer

    # Getter for orderDate (order date shouldn't change, so no setter)
    def get_order_date(self):
        return self._orderDate

    # Getter for order_items
    def get_order_items(self):
        return self._order_items

    # Add order item
    def add_order_item(self, order_item):
        self._order_items.append(order_item)

    # Calculate total amount for the order
    def get_total_amount(self):
        return sum(item.get_total_price() for item in self._order_items)

    # String representation of the Order
    def __str__(self):
        formatted_date = self._orderDate.strftime("%Y-%m-%d %H:%M:%S")
        items = "\n".join([str(item) for item in self._order_items])
        # Use getter to access customer details
        return f"Order(id={self._orderID}, customer={self.get_customer().customerName}, date={formatted_date}, total_amount={self.get_total_amount()}, items=[\n{items}\n])"
