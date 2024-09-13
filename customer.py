from payment import Payment
from order import Order
from decimal import Decimal

class Customer:
    nextID = 1000

    def __init__(self, name):
        self._customerID = Customer.nextID
        Customer.nextID += 1
        self._customerName = name
        self._customerBalance = Decimal('0.00')
        self._orders = []
        self._payments = []

    # Property for customerID (ID shouldn't change, so no setter)
    @property
    def customerID(self):
        return self._customerID

    # Property for customerName (with both getter and setter)
    @property
    def customerName(self):
        return self._customerName

    @customerName.setter
    def customerName(self, name):
        self._customerName = name

    # Property for customerBalance (read-only)
    @property
    def customerBalance(self):
        return self._customerBalance

    # Property for orders (read-only)
    @property
    def orders(self):
        return self._orders

    # Property for payments (read-only)
    @property
    def payments(self):
        return self._payments

    # Add an order and update balance
    def add_order(self, order):
        self._orders.append(order)
        self._customerBalance += Decimal(str(order.get_total_amount()))

    # Add a payment and update balance
    def add_payment(self, payment):
        self._payments.append(payment)
        self._customerBalance -= Decimal(str(payment.paymentAmount))

    # String representation of the Customer
    def __str__(self):
        return f"Customer(id={self._customerID}, name={self._customerName}, balance={self._customerBalance:.2f})"
