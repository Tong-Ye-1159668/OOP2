from controller import CompanyController

def main():
    company = CompanyController()

    # Load customers and products from files
    company.load_customers('customer.txt')
    company.load_products('product.txt')

    # Create an order for one of the customers and add order items
    order = company.create_order("Ignacia Craft")
    if order:
        company.add_order_item(order, "Post-it Notes", 2)
        company.add_order_item(order, "Blue Ballpoint Pens Box of 50", 1)
    else:
        print("Order creation failed!")

    # Submit the order and make payment
    company.submit_order(order)
    company.make_payment("Ignacia Craft", 50.0)

    # Print all customers, orders, and payments
    print("Customers:", company.list_all_customers())
    print("Orders:", company.list_all_orders())
    print("Payments:", company.list_all_payments())

if __name__ == "__main__":
    main()
