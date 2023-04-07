# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Item:
    def __init__(self, item_name):
        self.name = item_name

    def __str__(self):
        return f"Item Type: {self.name}"


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


def main_menu_list():
    print("You are in the Main Menu!")
    print("Please choose one of the following options")
    print("1. New Transaction")
    print("2. List of Products")
    print("3. Machine Status")
    print("4. Statistical Report")
    print("5. Reset")
    print("6. Exit")


def display_main_menu():
    menu_over = False

    while not menu_over:
        main_menu_list()
        choice = input("Select an Option: ")

        if str(choice).lower() == "6":
            print("Shutting Down now")
            menu_over = True
        if str(choice).lower() == "3" or str(choice).lower() == "4" or str(choice).lower() == "5":
            print("Admin Password (123): ")


def main_menu():
    display_main_menu()


def startup():
    print("Welcome to Monash University Vending Machine\n")
    display_main_menu()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    startup()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
