# This dictionary that contains all the menu items, their prices, and even includes the stock amount
menu_item = {
    'Fanta': {'price': 2.99, 'stock': 8},
    'Mirinda': {'price': 2.99, 'stock': 7},
    'Chocolate Milk': {'price': 2.49, 'stock': 6},
    'Strawberry Milk': {'price': 2.49, 'stock': 10},
    'Oman Chips': {'price': 0.99, 'stock': 10},
    'Coca Cola': {'price': 3.49, 'stock': 7},
    'Pepsi': {'price': 3.49, 'stock': 6},
    'Coca Cola Zero': {'price': 3.99, 'stock': 5},
    'Diet Pepsi': {'price': 3.99, 'stock': 5},
    'Snicker': {'price': 4.99, 'stock': 8},
    'Twix': {'price': 4.99, 'stock': 8},
}

def display_menu(menu_item):
    print("\n- - - Available Items - - -\n")
    for i, (item, details) in enumerate(menu_item.items(), start=1):
        stock = details['stock']
        price = details['price']
        print(f"{i}. {item} - ${price:.2f} (Stock: {stock})")

print("  _   _                _ _              ___  ___           _     _             \n | | | |              | (_)             |  \\/  |          | |   (_)            \n | | | | ___ _ __   __| |_ _ __   __ _  | .  . | __ _  ___| |__  _ _ __   ___  \n | | | |/ _ \\ '_ \\ / _` | | '_ \\ / _` | | |\\/| |/ _` |/ __| '_ \\| | '_ \\ / _ \\ \n \\ \\_/ /  __/ | | | (_| | | | | | (_| | | |  | | (_| | (__| | | | | | | |  __/ \n  \\___/ \\___|_| |_|\\__,_|_|_| |_|\\__, | \\_|  |_/\\__,_|\\___|_| |_|_|_| |_|\\___| \n                                 __/ |                                        \n                                |___/                                         \n")

# Ascii text for visuals

# Prompts the user for their initial balance and ensures the program doesn't exit on invalid input
while True:
    try:
        balance = float(input("Insert Your Cash Here (e.g., 1.99, 2.99, 3.99, 10, 25): $"))
        break  # Exits the loop if the input from the user is valid
    except ValueError:
        print("\nInvalid input! Please enter a numeric value.")

while balance > 0.98:
    # Displays the menu
    display_menu(menu_item)

    # Prompts user for item selection
    try:
        choice_num = int(input("\nPlease select an item by typing its number: "))
        if 1 <= choice_num <= len(menu_item):
            item = list(menu_item.keys())[choice_num - 1]
            details = menu_item[item]
            price = details['price']
            stock = details['stock']

            # Checks the stock and balance
            if stock > 0:
                if balance >= price:
                    # Deducts stock and balance
                    menu_item[item]['stock'] -= 1
                    balance -= price
                    print(f"\nYou have selected the {item} and have paid ${price:.2f}.")
                    print(f"Your remaining balance is: ${balance:.2f}")
                else:
                    print("\nInsufficient balance. Please insert more money.")
            else:
                print(f"\nSorry, {item} is out of stock. Please choose a different item.")
        else:
            print("\nInvalid selection. Please try again.")
    except ValueError:
        print("\nInvalid input! Please enter a valid number.")
        continue

    # Prompts user to continue shopping
    if balance > 0.98:
        continue_choice = input("\nWould you like to buy another item? (yes/no): ").lower()
        if continue_choice != "yes":
            print(f"\n- - - Thank you for purchasing! Your change is ${balance:.2f}. - - -")
            break
else:
    print("\n- - - You have run out of balance. Thank you for using the vending machine and have a nice day! - - -")