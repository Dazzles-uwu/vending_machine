class Payment:
    def __init__(self):
        self.inserted_coin = 0

    def __str__(self):
        return f"Amount of Coin User has paid: {self.inserted_coin}"

    def add_coins(self, inserted_amount):
        self.inserted_coin += inserted_amount

    def current_coin_amount_in_dollars(self):
        return "%.2f" % (self.inserted_coin/100)

    def current_coin_amount_in_cents(self):
        return self.inserted_coin


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

    def cart(self):
        return dict(self.cart_items)


class Machine:
    def __init__(self, status, coins):
        self.status = status
        self.coins = coins

    def __str__(self):
        return f"Machine Status: {self.status}\n" \
               f"Coin amount: {self.coins}"

    def check_coin_amount_in_machine(self):
        return int(self.coins)


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


cart = {
    "coffee": {"quantity": 23, "price": 2.20}
}

dict_of_items = {
    "coffee": {"stock": 200, "price": 2.20},
    "tea": {"stock": 0, "price": 2.20},
    "juice": {"stock": 405, "price": 2.20},
    "coke": {"stock": 32405, "price": 2.20}
}

user_payment = Payment()


def overall_cart_price():
    overall_price = 0
    for keys, values in cart.items():
        print(f'{keys.capitalize():8} Quantity: {values["quantity"]: 7}    Price: ${values["price"]}')
        overall_price += values["price"] * int(values["quantity"])
    return int("%.2f" % overall_price)


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


def insert_coins_into_machine():
    global user_payment
    while True:
        print("\nInsert Coin Menu")
        current_user_payment()
        print("Please choose one of the following options")
        print("1. Insert coin")
        print("2. Finish inserting coin / Back to Finalise Purchase Menu")
        option = input("What would you like to do?: ")
        if option == "1":
            print("\nPlease enter the coin value you wish to enter (20, 50, 100, 200) in cents")
            coin_value = input("Coin Value: ")
            if coin_value == "20" or coin_value == "50" or coin_value == "100" or coin_value == "200":
                print("You have entered:", coin_value)
                coin_amount = input("How many " + coin_value + " coins would you like to enter"
                                                               " in the vending machine?: ")
                if coin_amount.isdigit():
                    if int(coin_amount) < 0:
                        print("Amount cannot be lower than 0")
                    else:
                        user_payment.add_coins(int(coin_value) * int(coin_amount))
                else:
                    print("Not a valid Coin amount, please try again")
            else:
                print("Not a valid Coin value, please try again")
        elif option == "2":
            break
        else:
            print("Please enter a valid input")


def user_options_when_inserted_money_is_inefficient():
    while True:
        print("WARNING!\nYou have not entered required amount into the vending machine")
        print("Please choose one of the following")
        print("1. Refund Inserted Coins and Reset / Cancel current transaction")
        print("2. Re-Enter Coins / Back to previous Screen")
        options = input("What would you like to do?")

        if options == "1":
            print("Refund inserted coins")
        elif options == "2":
            continue_and_finalise_purchase()
            break


def validate_coins():
    print("Checking INSERTED COINS NOW")
    amount_user_paid = user_payment.current_coin_amount_in_cents()
    # give any change back and dispense items
    if amount_user_paid - overall_cart_price() >= 0:
        print("Dispensing")
        print("Congratulations you have purchased your items")
    else:
        user_options_when_inserted_money_is_inefficient()


def current_user_payment():
    print("\nCurrent Inserted Payment: " + "$" + user_payment.current_coin_amount_in_dollars(), "\n")


# Finalise Purchase menu
def continue_and_finalise_purchase():
    while True:
        chosen_items_plus_running_cost()
        current_user_payment()

        print("\nFinalise Purchase Menu")
        print("1. Continue to buy / Change Order")
        print("2. Insert Coins")
        print("3. Confirm and Continue (Dispense Item/s)")
        print("4. Refund Inserted Coins")
        print("5. Cancel / Reset Transaction")
        option = input("What would you like to do?: ")

        if option == "1":
            new_transaction(False)
            break
        elif option == "2":
            insert_coins_into_machine()
        elif option == "3":
            validate_coins()
            break
        elif option == "4":
            # Need to check if user has paid anything.
            print("REFUND INSERTED COINS")
        elif option == "5":
            cart.clear()
            print("Your cart has been cleared")
            new_transaction(True)
            break
        else:
            print("invalid choice")


# U-001 / New Transaction can be started
def new_transaction(is_new_transaction: bool):
    print("\nTransaction Menu")
    if is_new_transaction:
        print("Welcome to a new transaction")
    while True:
        chosen_items_plus_running_cost()
        display_list_of_products()
        print("Available Options")
        print("1. Add item to Cart")
        print("2. Remove item from Cart")
        print("3. List of Products")
        print("4. Continue / Finalise Order")
        print("5. Go back to Main Menu")
        print("6. Reset / Cancel current transaction")
        # NEED TO ADD Have an option to reset
        option = input("What would you like to do?: ")

        if option == "1" or option == "2":
            chosen_items_plus_running_cost()
            add_or_remove_items_from_cart(option)
        elif option == "3":
            display_list_of_products()
        elif option == "4":
            if cart:
                continue_and_finalise_purchase()
                break
            else:
                print("\nYou do NOT have any Items in your CART")
        elif option == "5":
            break
        # Allows users to reset /cancel the continuing transactions. It restarts the transaction
        elif option == "6":
            if cart:
                cart.clear()
                print("Your cart has been cleared")
                new_transaction(True)
                break
            else:
                print("\nYou do NOT have any ITEMS in your CART")
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
    print("5. Reset System")
    print("6. Exit\n")


def cancel_transaction_or_keep_previous_transaction():
    # prompt the user to choose whether keep previous transaction or start a new one
    while True:
        reset_or_keep = input("You have a previously saved transaction."
                              "Would you like to reset/cancel? (y/n)")
        if reset_or_keep == "n":
            new_transaction(True)
            break
        elif reset_or_keep == "y":
            cart.clear()
            new_transaction(True)
            break
        else:
            print("unknown input, please enter (y/n)")


def display_main_menu():
    menu_over = False

    while not menu_over:
        main_menu_list()
        choice = input("Select an Option: ")

        if str(choice).lower() == "1":
            # Need to check if the cart has items. If so, ask the user if they want to restart. Else keep the cart
            if cart:
                # if cart has items, go inside the function and ask what they want to do with the transaction
                cancel_transaction_or_keep_previous_transaction()
            else:
                # Start Transaction
                new_transaction(True)
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
