import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from controller import CompanyController


class Application(tk.Tk):
    def __init__(self, company):
        super().__init__()
        self.company = company
        self.title("Lincoln Office Supplies")
        self.geometry("880x600")

        # Load customers and products from files
        self.company.load_customers('customer.txt')
        self.company.load_products('product.txt')

        # Create UI components
        self.create_customer_frame()
        self.create_order_frame()
        self.create_payment_frame()
        self.create_display_frame()

        # Initialize order and customer variables
        self.current_order = None
        self.current_customer = None

    def create_customer_frame(self):
        customer_frame = tk.Frame(self, relief=tk.RIDGE, borderwidth=2)
        customer_frame.pack(pady=10, fill=tk.X)

        tk.Label(customer_frame, text="Select Customer:", font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Load customer names into OptionMenu
        customer_names = [customer.customerName for customer in self.company.customers] or ["No customers available"]
        self.customer_var = tk.StringVar(self)
        self.customer_var.set(customer_names[0])  # Default selection
        self.customer_menu = tk.OptionMenu(customer_frame, self.customer_var, *customer_names)
        self.customer_menu.grid(row=0, column=1, padx=10, pady=5)

        # Customer information display box
        self.customer_info = tk.Text(customer_frame, height=3, width=60, bg="lightyellow")
        self.customer_info.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # New order button
        tk.Button(customer_frame, text="New Order", command=self.new_order, font=('Arial', 12)).grid(row=0, column=2, padx=10, pady=5)

    def create_order_frame(self):
        order_frame = tk.Frame(self, relief=tk.RIDGE, borderwidth=2)
        order_frame.pack(pady=10, fill=tk.X)

        tk.Label(order_frame, text="Process Order", font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=10, pady=5, sticky="w")

        product_frame = tk.Frame(order_frame)
        product_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

        tk.Label(product_frame, text="Select Product:", font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Load product names into OptionMenu
        product_names = [product.productName for product in self.company.products] or ["No products available"]
        self.product_var = tk.StringVar(self)
        self.product_var.set(product_names[0])
        self.product_menu = tk.OptionMenu(product_frame, self.product_var, *product_names)
        self.product_menu.grid(row=0, column=1, padx=10, pady=5)

        # Quantity input
        tk.Label(product_frame, text="Quantity:", font=('Arial', 12)).grid(row=0, column=2, padx=10, pady=5)
        self.quantity_entry = tk.Entry(product_frame, width=10)  # 设置宽度，确保输入框可见
        self.quantity_entry.grid(row=0, column=3, padx=10, pady=5)

        # Add product button
        tk.Button(product_frame, text="Add Product", command=self.add_order_item, font=('Arial', 12)).grid(row=0, column=4, padx=10, pady=5)

        # Order details display box
        self.order_info = tk.Text(order_frame, height=8, width=70, bg="lightblue")
        self.order_info.grid(row=2, column=0, columnspan=5, padx=10, pady=10)

        # Submit order button
        tk.Button(order_frame, text="Submit Order", command=self.submit_order, font=('Arial', 12)).grid(row=3, column=4, padx=10, pady=5)

    def create_payment_frame(self):
        payment_frame = tk.Frame(self, relief=tk.RIDGE, borderwidth=2)
        payment_frame.pack(pady=10, fill=tk.X)

        tk.Label(payment_frame, text="Process Payment", font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=10, pady=5, sticky="w")

        tk.Label(payment_frame, text="Payment Amount:", font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=5)
        self.payment_entry = tk.Entry(payment_frame, width=15)  # 设置宽度，确保输入框可见
        self.payment_entry.grid(row=1, column=1, padx=10, pady=5)

        # Payment button
        tk.Button(payment_frame, text="Pay", command=self.process_payment, font=('Arial', 12)).grid(row=1, column=2, padx=10, pady=5)


    def create_display_frame(self):
        display_frame = tk.Frame(self)
        display_frame.pack(pady=10)

        # Action buttons
        tk.Button(display_frame, text="List Customer Orders", command=self.show_orders, font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(display_frame, text="List Customer Payments", command=self.show_payments, font=('Arial', 12)).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(display_frame, text="List All Customers", command=self.show_customers, font=('Arial', 12)).grid(row=0, column=2, padx=10, pady=5)
        tk.Button(display_frame, text="List All Orders", command=self.show_orders, font=('Arial', 12)).grid(row=0, column=3, padx=10, pady=5)
        tk.Button(display_frame, text="List All Payments", command=self.show_payments, font=('Arial', 12)).grid(row=0, column=4, padx=10, pady=5)
        tk.Button(display_frame, text="Exit", command=self.quit, font=('Arial', 12)).grid(row=0, column=5, padx=10, pady=5)

    def new_order(self):
        customer_name = self.customer_var.get()
        self.current_customer = self.company.find_customer_by_name(customer_name)
        if self.current_customer:
            self.current_order = self.company.create_order(customer_name)
            self.customer_info.delete(1.0, tk.END)
            self.customer_info.insert(tk.END, f"Customer ID: {self.current_customer.customerID}\n")
            self.customer_info.insert(tk.END, f"Name: {self.current_customer.customerName}\n")
            self.customer_info.insert(tk.END, f"Balance: {self.current_customer.customerBalance:.2f}\n")
            self.order_info.delete(1.0, tk.END)  # Clear previous order info
        else:
            messagebox.showerror("Error", "Please select a valid customer")

    def add_order_item(self):
        if not hasattr(self, 'current_order') or self.current_order is None:
            messagebox.showerror("Error", "Please create an order first")
            return

        product_name = self.product_var.get()
        quantity = self.quantity_entry.get()
        if not quantity.isdigit():
            messagebox.showerror("Error", "Quantity must be a valid number")
            return

        if int(quantity) <= 0:
            messagebox.showerror("Error", "Quantity must be greater than zero")
            return

        product = self.company.find_product_by_name(product_name)
        if product:
            self.company.add_order_item(self.current_order, product_name, int(quantity))
            self.order_info.insert(tk.END, f"{quantity} x {product_name} = {float(quantity) * product.productPrice:.2f}\n")
        else:
            messagebox.showerror("Error", "Product not found")

    def submit_order(self):
        if hasattr(self, 'current_order') and self.current_order:
            self.company.submit_order(self.current_order)
            self.order_info.insert(tk.END, "Order submitted successfully\n")
        
            self.current_order = None
        else:
            messagebox.showerror("Error", "No active order to submit")

    def process_payment(self):
        if not hasattr(self, 'current_customer') or self.current_customer is None:
            messagebox.showerror("Error", "Please select a valid customer")
            return

        payment_amount = self.payment_entry.get()
        try:
            amount = float(payment_amount)
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid payment amount")
            return

        self.company.make_payment(self.current_customer.customerName, amount)
        self.customer_info.delete(1.0, tk.END)
        self.customer_info.insert(tk.END, f"Customer ID: {self.current_customer.customerID}\n")
        self.customer_info.insert(tk.END, f"Name: {self.current_customer.customerName}\n")
        self.customer_info.insert(tk.END, f"Balance: {self.current_customer.customerBalance:.2f}\n")
        self.order_info.insert(tk.END, f"Payment of ${amount:.2f} made\n")

    def show_customers(self):
        customers = self.company.list_all_customers()  
        self.order_info.delete(1.0, tk.END)  
        if customers:
            self.order_info.insert(tk.END, "All Customers:\n" + "\n".join(customers) + "\n")
        else:
            self.order_info.insert(tk.END, "No customers available\n")

    def show_orders(self):
        orders = self.company.list_all_orders()  
        self.order_info.delete(1.0, tk.END)  
        if orders:
            self.order_info.insert(tk.END, "All Orders:\n" + "\n".join(orders) + "\n")
        else:
            self.order_info.insert(tk.END, "No orders available\n")

    def show_payments(self):
        payments = self.company.list_all_payments() 
        self.order_info.delete(1.0, tk.END)  
        if payments:
            self.order_info.insert(tk.END, "All Payments:\n" + "\n".join(payments) + "\n")
        else:
            self.order_info.insert(tk.END, "No payments available\n")


if __name__ == "__main__":
    company = CompanyController()
    app = Application(company)
    app.mainloop()
