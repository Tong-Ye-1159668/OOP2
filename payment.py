from datetime import datetime

class Payment:
    def __init__(self, customer, amount):
        self._customer = customer
        self._paymentAmount = amount
        self._paymentDate = datetime.now()

    # Getter and setter for customer
    def get_customer(self):
        return self._customer

    def set_customer(self, customer):
        self._customer = customer

    # Getter and setter for paymentAmount
    def get_payment_amount(self):
        return self._paymentAmount

    def set_payment_amount(self, amount):
        self._paymentAmount = amount

    # Getter for paymentDate (no setter as this should be immutable after creation)
    def get_payment_date(self):
        return self._paymentDate

    # String representation of the Payment object
    def __str__(self):
        formatted_date = self._paymentDate.strftime("%Y-%m-%d %H:%M:%S")
        return f"Payment(customer={self._customer.customerName}, amount={self._paymentAmount}, date={formatted_date})"
