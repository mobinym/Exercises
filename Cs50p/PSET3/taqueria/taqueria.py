menu = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

total = 0

while True:
    try:
        # Prompt the user for an item
        item = input("Enter an item: ").lower()

        # Check if the item is in the menu
        if item in menu:
            total += menu[item]
            print(f"Total: ${total:.2f}")

    except EOFError:
        # End the program when the user inputs control-d
        break
