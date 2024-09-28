import json

# List of products with their prices
product_list = {
    'Laptop': 42200,
    'Tablet': 17500,
    'iPhone': 57800,
    'Sound System': 7410
}

# Greeting message
print("Welcome to Pradhuman Planet!")
print("Here is the list of available products and their prices:")

# Display the product list with prices
for product, price in product_list.items():
    print(f"{product}: Rs{price}")

# Variables to track order total and summary
order_total = 0
order_summary = {}

# Discount criteria
discount_threshold = 100000  # Minimum total for discount
discount_rate = 0.1  # 10% discount

# Function to display all available products
def display_products():
    print("\nAvailable products:")
    for product, price in product_list.items():
        print(f"{product}: Rs{price}")

# Function to add products to the order
def add_to_order(product_name, quantity):
    global order_total
    if product_name in product_list:
        # Update the order summary and total price
        order_summary[product_name] = order_summary.get(product_name, 0) + quantity
        order_total += product_list[product_name] * quantity
        print(f"{quantity} unit(s) of '{product_name}' added to your order.")
    else:
        print(f"Sorry, '{product_name}' is not available.")

# Function to remove products from the order
def remove_from_order(product_name, quantity):
    global order_total
    if product_name in order_summary:
        if order_summary[product_name] >= quantity:
            # Reduce quantity or remove product from the order summary
            order_summary[product_name] -= quantity
            order_total -= product_list[product_name] * quantity
            if order_summary[product_name] == 0:
                del order_summary[product_name]
            print(f"{quantity} unit(s) of '{product_name}' removed from your order.")
        else:
            print(f"You cannot remove more than ordered. You only ordered {order_summary[product_name]} unit(s).")
    else:
        print(f"'{product_name}' is not in your order.")

# Function to apply discount if eligible
def apply_discount():
    global order_total
    if order_total >= discount_threshold:
        discount = order_total * discount_rate
        order_total -= discount
        print(f"Congratulations! You received a discount of Rs{discount:.2f}. Total after discount: Rs{order_total:.2f}")
    else:
        print(f"No discount applied. Your total is below the Rs{discount_threshold} threshold.")

# Function to save the order to a file
def save_order():
    with open('order.json', 'w') as f:
        json.dump(order_summary, f)
    print("Your order has been saved successfully!")

# Function to load an order from a saved file
def load_order():
    global order_summary, order_total
    try:
        with open('order.json', 'r') as f:
            order_summary = json.load(f)
            order_total = sum(product_list[product] * quantity for product, quantity in order_summary.items())
        print("Your saved order has been loaded successfully!")
    except FileNotFoundError:
        print("No saved order found!")

# Main order processing loop
while True:
    print("\nWhat would you like to do?")
    print("1. View all products")
    print("2. Add a product to your order")
    print("3. Remove a product from your order")
    print("4. View current order summary")
    print("5. Apply discount (if eligible)")
    print("6. Save order")
    print("7. Load saved order")
    print("8. Checkout and exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        display_products()
    elif choice == '2':
        product_name = input("Enter the name of the product to order: ")
        if product_name in product_list:
            try:
                quantity = int(input("Enter the quantity: "))
                if quantity > 0:
                    add_to_order(product_name, quantity)
                else:
                    print("Quantity must be a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number for quantity.")
        else:
            print(f"Sorry, '{product_name}' is not available.")
    elif choice == '3':
        product_name = input("Enter the name of the product to remove: ")
        if product_name in order_summary:
            try:
                quantity = int(input("Enter the quantity to remove: "))
                if quantity > 0:
                    remove_from_order(product_name, quantity)
                else:
                    print("Quantity must be a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number for quantity.")
        else:
            print(f"'{product_name}' is not in your order.")
    elif choice == '4':
        print("\nOrder Summary:")
        if order_summary:
            for product, quantity in order_summary.items():
                print(f"{product}: {quantity} unit(s) (Rs{product_list[product]} each)")
            print(f"Total cost: Rs{order_total}")
        else:
            print("No products in your order.")
    elif choice == '5':
        apply_discount()
    elif choice == '6':
        save_order()
    elif choice == '7':
        load_order()
    elif choice == '8':
        print("\nCheckout:")
        if order_summary:
            print("Final order summary:")
            for product, quantity in order_summary.items():
                print(f"{product}: {quantity} unit(s) (Rs{product_list[product]} each)")
            print(f"Total amount to pay: Rs{order_total}")
            apply_discount()  # Final discount application before checkout
        else:
            print("You have not ordered anything.")
        print("Thank you for shopping at Pradhuman Planet! Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
