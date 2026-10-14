# College Canteen Food Ordering System

menu = {
    "Sandwich": 50,
    "Burger": 80,
    "Juice": 30,
    "Dosa": 40
}


def display_menu():
    return menu


def add_to_cart(cart, item, quantity):
    if item not in menu:
        raise ValueError("Food item not available")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    cart[item] = cart.get(item, 0) + quantity
    return cart


def calculate_total(cart):
    total = 0

    for item, quantity in cart.items():
        if item not in menu:
            raise ValueError("Food item not available")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        total += menu[item] * quantity

    return total


def place_order(cart):
    if not cart:
        raise ValueError("Cart is empty")

    total = calculate_total(cart)
    return "Order placed successfully! Total: Rs." + str(total)