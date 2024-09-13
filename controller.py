from customer import Customer
from product import Product
from order import Order
from orderitem import OrderItem
from payment import Payment
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CompanyController:
    def __init__(self):
        self.customers = []
        self.products = []

    def load_customers(self, file_path):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    customer_name = line.strip()
                    self.add_customer(customer_name)
            logging.info(f"Loaded customers from {file_path}")
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            print(f"File not found: {file_path}")
        except Exception as e:
            logging.error(f"An error occurred while loading customers: {e}")
            print(f"An error occurred while loading customers: {e}")

    def load_products(self, file_path):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    try:
                        product_info = line.strip().split(", ")
                        product_name = product_info[0]
                        product_price = float(product_info[1])
                        self.add_product(product_name, product_price)
                    except (ValueError, IndexError) as e:
                        logging.warning(f"Error parsing product line: {line}. Error: {e}")
                        print(f"Error parsing product line: {line}. Error: {e}")
            logging.info(f"Loaded products from {file_path}")
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            print(f"File not found: {file_path}")
        except Exception as e:
            logging.error(f"An error occurred while loading products: {e}")
            print(f"An error occurred while loading products: {e}")

    def add_customer(self, name):
        if self.find_customer_by_name(name):
            logging.warning(f"Customer {name} already exists.")
            print(f"Customer {name} already exists.")
            return None
        customer = Customer(name)
        self.customers.append(customer)
        logging.info(f"Added customer {name}")
        return customer

    def add_product(self, name, price):
        if self.find_product_by_name(name):
            logging.warning(f"Product {name} already exists.")
            print(f"Product {name} already exists.")
            return None
        product = Product(name, price)
        self.products.append(product)
        logging.info(f"Added product {name} with price {price}")
        return product

    def find_customer_by_name(self, name):
        for customer in self.customers:
            if customer.customerName == name:
                return customer
        return None

    def find_product_by_name(self, name):
        for product in self.products:
            if product.productName == name:
                return product
        return None

    def create_order(self, customer_name):
        customer = self.find_customer_by_name(customer_name)
        if customer:
            order = Order(customer)
            customer.add_order(order)
            logging.info(f"Created order for customer {customer_name}")
            return order
        logging.error(f"Customer {customer_name} not found.")
        print(f"Customer {customer_name} not found.")
        return None

    def add_order_item(self, order, product_name, quantity):
        if quantity <= 0:
            logging.warning(f"Invalid quantity {quantity} for product {product_name}. Must be greater than zero.")
            print("Quantity must be more than zero.")
            return
        product = self.find_product_by_name(product_name)
        if product:
            order_item = OrderItem(product, quantity)
            order.add_order_item(order_item)
            logging.info(f"Added {quantity} of {product_name} to order {order.get_order_id()}")
        else:
            logging.error(f"Product {product_name} not found.")
            print(f"Product {product_name} not found.")

    def submit_order(self, order):
        logging.info(f"Order {order.get_order_id()} submitted for customer {order.get_customer().customerName}")


    def make_payment(self, customer_name, amount):
        if amount <= 0:
            logging.warning(f"Invalid payment amount {amount} for customer {customer_name}. Must be positive.")
            print("Payment amount must be positive.")
            return None
        customer = self.find_customer_by_name(customer_name)
        if customer:
            payment = Payment(customer, amount)
            customer.add_payment(payment)
            logging.info(f"Processed payment of {amount} for customer {customer_name}")
            return payment
        logging.error(f"Customer {customer_name} not found.")
        print(f"Customer {customer_name} not found.")
        return None

    def list_all_customers(self):
        logging.info("Listing all customers")
        return [str(customer) for customer in self.customers]

    def list_all_orders(self):
        logging.info("Listing all orders")
        orders = []
        for customer in self.customers:
            orders.extend([str(order) for order in customer.orders])
        return orders

    def list_all_payments(self):
        logging.info("Listing all payments")
        payments = []
        for customer in self.customers:
            payments.extend([str(payment) for payment in customer.payments])
        return payments
