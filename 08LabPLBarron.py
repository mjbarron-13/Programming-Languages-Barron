# Function 1: add_to_stock(stock_list)

def add_to_stock(stock_list):
    stock_list.append(75)
    print("Inside function (stock):", stock_list)

# Inventory list before function call
inventory = [100, 200, 150]

# Call the function
add_to_stock(inventory)

# Print inventory after function call
print("Outside function (stock):", inventory)

# Function 2: update_price(price)

def update_price(price):
    new_price = price + (price * 0.10)
    print("Inside function (price):", new_price)

# Base price before function call
base_price = 250.0

# Call the function
update_price(base_price)

# Print base_price after function call
print("Outside function (price):", base_price)
