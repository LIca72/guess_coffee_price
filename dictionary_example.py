# Dictionary example in Python

coffee_menu = {
    "latte": "milk coffee",
    "espresso": "strong black coffee",
    "americano": "watered espresso",
    "cappuccino": "coffee with milk foam"
}

print("Latte is:", coffee_menu["latte"])


coffee_menu["mocha"] = "chocolate coffee"


coffee_menu["latte"] = "coffee with milk"


del coffee_menu["espresso"]

print("\nFull Coffee Menu:")
for coffee, description in coffee_menu.items():
    print(f"{coffee.title()}: {description}")
