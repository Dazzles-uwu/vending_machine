# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
cart = {
    "coffee": {"quantity": 23, "price": 2.20}
}

dict_of_items = {
    "coffee": {"stock": 200, "price": 2.20},
    "tea": {"stock": 0, "price": 2.20},
    "juice": {"stock": 405, "price": 2.20},
    "coke": {"stock": 32405, "price": 2.20}
}


class Item:
    def __init__(self, item_name, item_stock, item_price):
        self.name = item_name
        self.stock = item_stock
        self.price = item_price

    def __str__(self):
        return f"Item Type: {self.name}\n" \
               f"Stock Amt.: {self.stock}\n" \
               f"Item Price: {self.price}\n"


class Cart:
    def __init__(self, cart_items: dict):
        self.cart_items = cart_items

    def __str__(self):
        return f"Cart contains: {self.cart_items}"


class Machine:
    def __init__(self, status):
        self.status = status

    def __str__(self):
        return f"Machine Status: {self.status}"


class Transaction:
    def __init__(self, items_purchased, date, payment):
        self.items_purchased = items_purchased
        self.date = date
        self.payment = payment

    def __str__(self):
        return f"Transaction\n" \
               f"Items Purchased: {self.items_purchased}\n" \
               f"Date Purchased: {self.date}\n" \
               f"Payment amount: {self.payment}\n"


# Running Cost of the product must be shown to the user i.e. total cost of the purchase. U-003
def chosen_items_plus_running_cost():
    print("\nItems currently in cart:")
    if not cart:
        print("NO ITEMS CURRENTLY IN YOUR CART")
    else:
        overall_price = 0
        for keys, values in cart.items():
            print(f'{keys.capitalize():8} Quantity: {values["quantity"]: 7}    Price: ${values["price"]}')
            overall_price += values["price"] * int(values["quantity"])
        print("Total Price: $", overall_price)


# Add or remove an item from the Cart
def add_or_remove_items_from_cart(add_or_remove_option):
    item_has_been_chosen = False
    item_quantity_has_been_chosen = False

    # Checks if there is nothing in Cart and User chose to remove an item
    if not cart and add_or_remove_option == "2":
        print("There is NOTHING in your CART to remove!")
        return None

    while not item_has_been_chosen:
        if add_or_remove_option == "1":
            print("What ITEM would you like to be ADDED into your Cart?")
        elif add_or_remove_option == "2":
            print("What ITEM would you like to be REMOVED into your Cart?")
        else:
            print("Not a Valid option")
        item_chosen = input("Item: ").lower()

        if add_or_remove_option == "1":
            if item_chosen in dict_of_items.keys():
                while not item_quantity_has_been_chosen:
                    print("How many", item_chosen, "would you like to be ADDED to your cart?")
                    quantity_to_be_added = input("Quantity to be ADDED")
                    if quantity_to_be_added.isdigit():
                        # checks if there are enough stocks to buy
                        if dict_of_items[item_chosen]["stock"] - int(quantity_to_be_added) >= 0:
                            # if item has already been added to the cart, simply add the quantity user wants
                            if item_chosen in cart.keys():
                                cart[item_chosen]["quantity"] += int(quantity_to_be_added)
                            # if the item has NOT been added to the cart, create a key and its value
                            else:
                                cart[item_chosen] = {
                                    "quantity": int(quantity_to_be_added),
                                    "price": dict_of_items[item_chosen]["price"]
                                    }
                            item_has_been_chosen = True
                            item_quantity_has_been_chosen = True
                        # If there are no stocks available to buy, it will not allow purchase
                        elif dict_of_items[item_chosen]["stock"] <= 0:
                            print("There are currently NO stock of", item_chosen, "left")
                            item_has_been_chosen = True
                            item_quantity_has_been_chosen = True
                        else:
                            print("Not enough stock to add")
                    else:
                        print("Must be a number")
            else:
                print("Not a Valid item")
        elif add_or_remove_option == "2":
            if item_chosen in cart.keys():
                while not item_quantity_has_been_chosen:
                    print("How many", item_chosen, "would you like to be REMOVED to your cart?")
                    quantity_to_be_removed = input("Quantity to be REMOVED")
                    if quantity_to_be_removed.isdigit():
                        # Subtracts the amount of quantity in the cart
                        if cart[item_chosen]["quantity"] - int(quantity_to_be_removed) > 0:
                            cart[item_chosen]["quantity"] -= int(quantity_to_be_removed)
                            item_has_been_chosen = True
                            item_quantity_has_been_chosen = True
                        # Removes the item from the Cart entirely
                        elif cart[item_chosen]["quantity"] - int(quantity_to_be_removed) == 0:
                            del cart[item_chosen]
                            item_has_been_chosen = True
                            item_quantity_has_been_chosen = True
                        else:
                            print("Quantity cannot go below 0")
                    else:
                        print("Must be a number")
            else:
                print("Not a Valid item")


# U-001 / New Transaction can be started
def new_transaction():
    # Temp cart dict until a class is implemented

    print("Welcome to a new transaction")
    while True:
        chosen_items_plus_running_cost()
        display_list_of_products()
        print("Available Options")
        print("1. Add item to Cart")
        print("2. Remove item from Cart")
        print("3. Continue / Finalise Order")
        print("4. Cancel / Reset Transaction")
        option = input("What would you like to do?: ")

        if option == "1" or option == "2":
            chosen_items_plus_running_cost()
            add_or_remove_items_from_cart(option)
        elif option == "4":
            break
        else:
            print("Invalid choice")


# HardCoded for now / U-002 / S-002
def display_list_of_products():
    print("\nList of Vending Machine Products")
    for keys, values in dict_of_items.items():
        if int(values["stock"]) <= 0:
            print(f'{keys.capitalize():8} ALERT PRODUCT OUT OF STOCK')
        else:
            print(f'{keys.capitalize():8} Available Amount:{values["stock"]: 7}    Price: ${values["price"]}')
    print("\n")


def main_menu_list():
    print("\nYou are in the Main Menu!")
    print("Please choose one of the following options")
    print("1. New Transaction")
    print("2. List of Products")
    print("3. Machine Status")
    print("4. Statistical Report")
    print("5. Reset")
    print("6. Exit\n")


def display_main_menu():
    menu_over = False

    while not menu_over:
        main_menu_list()
        choice = input("Select an Option: ")

        if str(choice).lower() == "1":
            # Start Transaction
            new_transaction()
        elif str(choice).lower() == "2":
            # Display List
            display_list_of_products()
        elif str(choice).lower() == "3" or str(choice).lower() == "4" or str(choice).lower() == "5":
            password_input = input("Admin Password (123): ")
            # Continue depending on the variable "Choice"
            # if password_input == "123":
        elif str(choice).lower() == "6":
            print("Shutting Down now")
            menu_over = True


def main_menu():
    display_main_menu()


def startup():
    print("Welcome to Monash University Vending Machine\n")
    display_main_menu()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    startup()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
