def calculate_total(cart_items):
    if not cart_items:
        print("Cart is empty.")
        return 0
    total_price = sum(cart_items.values())
    if len(cart_items) > 5:
        discount = total_price * 0.10
        total_price -= discount
    return total_price

cart_items = {}
n = int(input("Enter number of items in the cart: "))
for i in range(n):
    item_name = input(f"Enter name of item {i+1}: ")
    try:
        item_price = float(input(f"Enter price of {item_name}: "))
    except ValueError:
        print("Invalid price entered. Skipping item.")
        continue
    cart_items[item_name] = item_price
total = calculate_total(cart_items)
print("Total Price:", total)
