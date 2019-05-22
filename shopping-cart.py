"""
iterate through a list of item costs in shopping cart
add them together and show the total in the terminal
"""

cart = [1.00, 3.50, 4.50, 10.00, 10.00, 30.00, 2.75]
total = 0

for item in cart:
    print(f"Item cost... {item}")
    total += item

print(f"Total cost of {cart.count} items... ${total}")