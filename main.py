# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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
    def __init__(self, list_of_items):
        self.cart_items = list_of_items

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
    cart = {
        "coffee": {"quantity": 3, "price": 2.20},
        "tea": {"quantity": 1, "price": 2.20},
        "juice": {"quantity": 5, "price": 2.20}
    }

    print("\nItems currently in cart:")
    if not cart:
        print("NO ITEMS CURRENTLY IN YOUR CART")
    else:
        overall_price = 0
        for keys, values in cart.items():
            print(f'{keys.capitalize():8} Quantity: {values["quantity"]: 7}    Price: ${values["price"]}')
            overall_price += values["price"] * int(values["quantity"])
        print("Total Price: $", overall_price)


# U-001 / New Transaction can be started
def new_transaction():
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

        if option == "4":
            break
        else:
            print("Invalid choice")


# HardCoded for now / U-002 / S-002
def display_list_of_products():
    dict_of_items = {
        "coffee": {"stock": 200, "price": 2.20},
        "tea": {"stock": 0, "price": 2.20},
        "juice": {"stock": 405, "price": 2.20},
        "coke": {"stock": 32405, "price": 2.20}
    }

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
