import datetime
import time
from tqdm import tqdm


class Payment:
    def __init__(self):
        self.inserted_coin = 0

    def __str__(self):
        return f"Amount of Coin User has paid: {self.inserted_coin}"

    def add_coins(self, inserted_amount):
        self.inserted_coin += inserted_amount

    def current_coin_amount_in_dollars(self):
        return "%.2f" % (self.inserted_coin / 100)

    def current_coin_amount_in_cents(self):
        return self.inserted_coin

    def reset_payment(self):
        self.inserted_coin = 0


class Item:
    def __init__(self):
        with open('items.txt', 'r') as f:
            self.items = {}
            for line in f:
                x = line.split(",")
                x[-1] = x[-1].strip()
                item_name = x[0]
                stock_key = x[1]
                stock_value = x[2]
                price_key = x[3]
                price_value = x[4]
                self.items[item_name] = {stock_key: int(stock_value), price_key: float(price_value)}

    def __str__(self):
        return f"Item Dictionary: {self.items}\n"

    def get_items(self):
        return self.items

    def display_list_of_products(self):
        print("\nList of Vending Machine Products")
        for keys, values in self.items.items():
            if int(values["stock"]) <= 0:
                print(f'{keys.capitalize():8} ALERT PRODUCT OUT OF STOCK')
            else:
                print(f'{keys.capitalize():8} Available Amount:{values["stock"]: 7}    '
                      f'Price: ${"%.2f" % values["price"]}')
        print("\n")

    def update_item_stock(self, cart_items):
        # Check cart and see what gets updated
        for key in cart_items:
            if key in self.items:
                if self.items[key]["stock"] - cart_items[key]["quantity"] <= 0:
                    del self.items[key]
                else:
                    self.items[key]["stock"] -= cart_items[key]["quantity"]

        with open('items.txt', 'w') as file:
            for key, value in self.items.items():
                file.write(str(key) + "," + "stock" + "," + str(value["stock"]) + "," + "price" + ","
                           + str(value["price"]) + "\n")

    def reset_items_to_default(self):
        with open('items.txt', 'w') as file:
            for key, value in self.items.items():
                file.write(str(key) + "," + "stock" + "," + str(300) + "," + "price" + ","
                           + str(value["price"]) + "\n")

        with open('items.txt', 'r') as f:
            self.items = {}
            for line in f:
                x = line.split(",")
                x[-1] = x[-1].strip()
                item_name = x[0]
                stock_key = x[1]
                stock_value = x[2]
                price_key = x[3]
                price_value = x[4]
                self.items[item_name] = {stock_key: int(stock_value), price_key: float(price_value)}


class Cart:
    def __init__(self):
        self.cart_items = {}

    def __str__(self):
        return f"Cart contains: {self.cart_items}"

    def get_cart(self):
        return dict(self.cart_items)

    def list_of_keys(self):
        return list(self.cart_items.keys())

    def reset_cart(self):
        self.cart_items.clear()

    def overall_cart_price_in_cents(self):
        overall_price = 0
        for keys, values in self.cart_items.items():
            overall_price += values["price"] * int(values["quantity"])
        return int(overall_price * 100)

    # Running Cost of the product must be shown to the user i.e. total cost of the purchase. U-003
    def chosen_items_plus_running_cost(self):
        print("\nItems currently in cart:")
        if not self.cart_items:
            print("NO ITEMS CURRENTLY IN YOUR CART")
        else:
            overall_price = 0
            for keys, values in self.cart_items.items():
                print(f'{keys.capitalize():8} Quantity: {values["quantity"]: 7}    Price: ${"%.2f" % values["price"]}')
                overall_price += values["price"] * int(values["quantity"])
            print("Total Price: $", "%.2f" % overall_price)

    def dispensed_items(self):
        print("\nDispensing the following item/s: ")
        for keys, values in self.cart_items.items():
            print(f'{keys.capitalize():8} Quantity: {values["quantity"]: 7}')
        print("Thank you and come again!")

    # Add or remove an item from the Cart
    def add_or_remove_items_from_cart(self, add_or_remove_option, items_available):
        item_has_been_chosen = False
        item_quantity_has_been_chosen = False

        # Checks if there is nothing in Cart and User chose to remove an item
        if not self.cart_items and add_or_remove_option == "2":
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
                if item_chosen in items_available.keys():
                    while not item_quantity_has_been_chosen:
                        print("How many", item_chosen, "would you like to be ADDED to your cart?")
                        quantity_to_be_added = input("Quantity to be ADDED")
                        if quantity_to_be_added.isdigit():
                            # checks if there are enough stocks to buy
                            if items_available[item_chosen]["stock"] - int(quantity_to_be_added) >= 0:
                                # if item has already been added to the cart, simply add the quantity user wants
                                if item_chosen in self.cart_items.keys():
                                    self.cart_items[item_chosen]["quantity"] += int(quantity_to_be_added)
                                # if the item has NOT been added to the cart, create a key and its value
                                else:
                                    self.cart_items[item_chosen] = {
                                        "quantity": int(quantity_to_be_added),
                                        "price": items_available[item_chosen]["price"]
                                    }
                                item_has_been_chosen = True
                                item_quantity_has_been_chosen = True
                            # If there are no stocks available to buy, it will not allow purchase
                            elif items_available[item_chosen]["stock"] <= 0:
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
                if item_chosen in self.cart_items.keys():
                    while not item_quantity_has_been_chosen:
                        print("How many", item_chosen, "would you like to be REMOVED to your cart?")
                        quantity_to_be_removed = input("Quantity to be REMOVED")
                        if quantity_to_be_removed.isdigit():
                            # Subtracts the amount of quantity in the cart
                            if self.cart_items[item_chosen]["quantity"] - int(quantity_to_be_removed) > 0:
                                self.cart_items[item_chosen]["quantity"] -= int(quantity_to_be_removed)
                                item_has_been_chosen = True
                                item_quantity_has_been_chosen = True
                            # Removes the item from the Cart entirely
                            elif self.cart_items[item_chosen]["quantity"] - int(quantity_to_be_removed) == 0:
                                del self.cart_items[item_chosen]
                                item_has_been_chosen = True
                                item_quantity_has_been_chosen = True
                            else:
                                print("Quantity cannot go below 0")
                        else:
                            print("Must be a number")
                else:
                    print("Not a Valid item")


class Machine:
    def __init__(self):
        with open('machine.txt', 'r') as f:
            for index, line in enumerate(f):
                if index == 0:
                    self.status = line.strip()
                elif index == 1:
                    self.coins = int(line.strip())

    def __str__(self):
        return f"Machine Status: {self.status}\n" \
               f"Coin amount: {self.coins}"

    def check_coin_amount_in_machine_in_cents(self):
        return int(self.coins)

    def get_machine_status(self):
        return self.status

    def set_maintenance_status(self):
        with open('machine.txt', 'r') as file:
            # read a list of lines into data
            data = file.readlines()

        # now change the 2nd line, note that you have to add a newline
        data[0] = "maintenance\n"
        data[1] = str(self.coins)

        # and write everything back
        with open('machine.txt', 'w') as file:
            file.writelines(data)

        with open('machine.txt', 'r') as file:
            # read updated changes
            data = file.readlines()
            self.status = data[0].strip()
            self.coins = int(data[1].strip())

    def set_working_status(self):
        with open('machine.txt', 'r') as file:
            # read a list of lines into data
            data = file.readlines()

        # now change the 2nd line, note that you have to add a newline
        data[0] = "working\n"
        data[1] = str(self.coins)

        # and write everything back
        with open('machine.txt', 'w') as file:
            file.writelines(data)

        with open('machine.txt', 'r') as file:
            # read updated changes
            data = file.readlines()
            self.status = data[0].strip()
            self.coins = int(data[1].strip())

    def give_change_to_consumers(self, change_amount):
        self.coins -= change_amount
        with open('machine.txt', 'r') as file:
            # read a list of lines into data
            data = file.readlines()

        # now change the 2nd line, note that you have to add a newline
        data[1] = str(self.coins)

        # and write everything back
        with open('machine.txt', 'w') as file:
            file.writelines(data)

        with open('machine.txt', 'r') as file:
            # read updated changes
            data = file.readlines()
            self.status = data[0].strip()
            self.coins = int(data[1].strip())

    def update_to_add_coin_stock(self, inserted_coins):
        with open('machine.txt', 'r') as file:
            # read a list of lines into data
            data = file.readlines()

        # now change the 2nd line, note that you have to add a newline
        data[1] = self.coins + inserted_coins
        data[1] = str(data[1])

        # and write everything back
        with open('machine.txt', 'w') as file:
            file.writelines(data)

        with open('machine.txt', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
            self.status = data[0].strip()
            self.coins = int(data[1].strip())

    def reset_items_to_default(self):
        with open('machine.txt', 'w') as file:
            file.writelines(self.status + "\n" + "50000")

        with open('machine.txt', 'r') as file:
            # read updated changes
            data = file.readlines()
            self.status = data[0].strip()
            self.coins = int(data[1].strip())


class Transaction:
    def __init__(self):
        with open('transaction.txt', 'r') as f:
            self.transaction_dict = {}
            key_id = 0
            for line in f:
                amount_of_items = 0
                temp_list_var = line.split(",")
                temp_list_var[-1] = temp_list_var[-1].strip()

                self.transaction_dict[key_id] = {}
                current_key_value = ""

                for index_transaction in temp_list_var:
                    if index_transaction == "items" or index_transaction == "payment" or index_transaction == "date":
                        current_key_value = index_transaction
                    elif current_key_value == "items":
                        if amount_of_items == 0:
                            self.transaction_dict[key_id]["items"] = [index_transaction]
                            amount_of_items += 1
                        else:
                            self.transaction_dict[key_id]["items"].append(index_transaction)
                    elif current_key_value == "payment":
                        self.transaction_dict[key_id]["payment"] = int(index_transaction)
                    elif current_key_value == "date":
                        self.transaction_dict[key_id]["date"] = index_transaction.strip()
                key_id += 1

    def __str__(self):
        return f"Transaction: {self.transaction_dict}"

    def get_transaction(self):
        return self.transaction_dict

    def record_transaction(self, cart_item_keys, cart_price):
        with open('transaction.txt', 'a') as file:
            string_of_items_in_cart = (','.join(cart_item_keys)).strip()
            x = datetime.datetime.now()

            file.write("\nitems" + "," + string_of_items_in_cart + "," + "payment" + ","
                       + str(cart_price) + "," + "date" + ","
                       + x.strftime("%A %d/%B/%Y %H:%M").strip())

        with open('transaction.txt', 'r') as f:
            self.transaction_dict = {}
            key_id = 0
            for line in f:
                amount_of_items = 0
                temp_list_var = line.split(",")
                temp_list_var[-1] = temp_list_var[-1].strip()

                self.transaction_dict[key_id] = {}
                current_key_value = ""

                for index_transaction in temp_list_var:
                    if index_transaction == "items" or index_transaction == "payment" or index_transaction == "date":
                        current_key_value = index_transaction
                    elif current_key_value == "items":
                        if amount_of_items == 0:
                            self.transaction_dict[key_id]["items"] = [index_transaction]
                            amount_of_items += 1
                        else:
                            self.transaction_dict[key_id]["items"].append(index_transaction)
                    elif current_key_value == "payment":
                        self.transaction_dict[key_id]["payment"] = int(index_transaction)
                    elif current_key_value == "date":
                        self.transaction_dict[key_id]["date"] = index_transaction.strip()
                key_id += 1


class Ingredient:
    def __init__(self):
        with open('ingredients.txt', 'r') as f:
            self.ingredient_dict = {}
            for line in f:
                temp_list_var = line.split(",")
                temp_list_var[-1] = temp_list_var[-1].strip()
                self.ingredient_dict[temp_list_var[0]] = int(temp_list_var[1])

    def get_ingredients(self):
        return dict(self.ingredient_dict)

    def take_away_ingredient(self):
        for key, value in self.ingredient_dict.items():
            if value > 0:
                self.ingredient_dict[key] = int(value) - 1

        with open('ingredients.txt', 'w') as file:
            for key, value in self.ingredient_dict.items():
                file.write(str(key) + "," + str(value) + "\n")

    def reset_items_to_default(self):
        with open('ingredients.txt', 'w') as file:
            for key, value in self.ingredient_dict.items():
                file.write(str(key) + "," + str("300") + "\n")

        with open('ingredients.txt', 'r') as f:
            self.ingredient_dict = {}
            for line in f:
                temp_list_var = line.split(",")
                temp_list_var[-1] = temp_list_var[-1].strip()
                self.ingredient_dict[temp_list_var[0]] = int(temp_list_var[1])


items = Item()
user_payment = Payment()
cart = Cart()
machine = Machine()
transaction = Transaction()
ingredient = Ingredient()


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


def refund_user_money():
    money_to_refund = user_payment.current_coin_amount_in_dollars()
    print("\n$" + money_to_refund, "has been refunded back to you.")
    print("Please come again soon\n")
    user_payment.reset_payment()


def user_options_when_inserted_money_is_inefficient():
    while True:
        print("WARNING!\nYou have not entered required amount into the vending machine")
        print("Please choose one of the following")
        print("1. Reset / Cancel current transaction (will refund inserted coins)")
        print("2. Re-Enter Coins / Back to previous Screen")
        options = input("What would you like to do?")

        if options == "1":
            if user_payment.current_coin_amount_in_cents() > 0:
                refund_user_money()
            new_transaction(True)
            break
        elif options == "2":
            continue_and_finalise_purchase()
            break
        else:
            print("Invalid options")


def return_change_after_dispensing(expected_change):
    # Check how much money is in the machine
    machine_coin_stock_availability = machine.check_coin_amount_in_machine_in_cents() - expected_change
    if machine_coin_stock_availability >= 0:
        machine.update_to_add_coin_stock(user_payment.current_coin_amount_in_cents())
        machine.give_change_to_consumers(expected_change)
        print("We have given you a CHANGE of", "$%.2f" % (expected_change / 100))
        print("Dispensing...")
        for i in tqdm(range(10)):
            time.sleep(1)
        cart.dispensed_items()
        # Maintain Drink Stock
        items.update_item_stock(cart.get_cart())
        # Record Transaction
        transaction.record_transaction(cart.list_of_keys(), cart.overall_cart_price_in_cents())
        # Reset cart
        cart.reset_cart()
        user_payment.reset_payment()
        print("Congratulations you have purchased your items")
        print("Goodbye, your transaction has ended")
    else:
        print("We currently do not have any change for you!")
        print("Please give exact change or kindly wait until the machine's money are stocked again")
        print("We will refund you your inserted Coins, please try again soon!")
        refund_user_money()
        continue_and_finalise_purchase()


def check_if_hot_items_in_cart():
    hot_item = False
    for item_name in cart.get_cart().keys():
        if item_name == "coffee" or item_name == "tea":
            hot_item = True

    if hot_item:
        print("Boiling....")
        for i in tqdm(range(10)):
            time.sleep(1)

        print("Mixing Ingredients....")
        for i in tqdm(range(10)):
            time.sleep(1)

        print("Your Hot item has been created, enjoy")
        # take away ingredient
        ingredient.take_away_ingredient()


def prompt_for_ingredients():
    no_ingredient = False
    for keys, values in ingredient.get_ingredients().items():
        if int(values) == 0:
            no_ingredient = True
            print("There are currently NO", keys, "available")
    while True:
        if no_ingredient:
            print("\nYou are still able to proceed to buy the item/s")
            print("however the missing ingredient/s will not be added")
            print("\nYour options are:")
            print("1. Continue to purchase without missing ingredient/s")
            print("2. Cancel Transaction")
            option = input("\nWhat would you like to do:")

            if option == "1":
                print("Continuing purchase...")
                no_ingredient = False
                break
            elif option == "2":
                if user_payment.current_coin_amount_in_cents() > 0:
                    refund_user_money()
                cart.reset_cart()
                print("Your cart has been cleared")
                new_transaction(True)
                no_ingredient = True
                break
            else:
                print("Invalid choice/input")
        else:
            break
    return no_ingredient


def validate_coins():
    print("Checking INSERTED COINS NOW")
    amount_user_paid = user_payment.current_coin_amount_in_cents()
    # give any change back and dispense items
    difference_in_money_inserted_and_cart_price = amount_user_paid - cart.overall_cart_price_in_cents()
    if difference_in_money_inserted_and_cart_price >= 0:
        if prompt_for_ingredients():
            return
        check_if_hot_items_in_cart()
        if difference_in_money_inserted_and_cart_price > 0:
            return_change_after_dispensing(difference_in_money_inserted_and_cart_price)
        else:
            print("Dispensing...")
            for i in tqdm(range(10)):
                time.sleep(1)
            cart.dispensed_items()
            # Maintain Coin stock
            machine.update_to_add_coin_stock(amount_user_paid)
            # Maintain Drink Stock
            items.update_item_stock(cart.get_cart())
            # Record Transaction
            transaction.record_transaction(cart.list_of_keys(), cart.overall_cart_price_in_cents())
            # Reset cart
            cart.reset_cart()
            user_payment.reset_payment()
            print("Congratulations you have purchased your items")
            print("Goodbye, your transaction has ended")
    else:
        user_options_when_inserted_money_is_inefficient()


def current_user_payment():
    print("\nCurrent Inserted Payment: " + "$" + user_payment.current_coin_amount_in_dollars(), "\n")


# Finalise Purchase menu
def continue_and_finalise_purchase():
    while True:
        cart.chosen_items_plus_running_cost()
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
            if user_payment.current_coin_amount_in_cents() > 0:
                refund_user_money()
            else:
                print("You have no money to be refunded")
        elif option == "5":
            if user_payment.current_coin_amount_in_cents() > 0:
                refund_user_money()
            cart.reset_cart()
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
        cart.chosen_items_plus_running_cost()
        items.display_list_of_products()
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
            cart.chosen_items_plus_running_cost()
            cart.add_or_remove_items_from_cart(option, items.get_items())
        elif option == "3":
            items.display_list_of_products()
        elif option == "4":
            if cart.get_cart():
                continue_and_finalise_purchase()
                break
            else:
                print("\nYou do NOT have any Items in your CART")
        elif option == "5":
            if user_payment.current_coin_amount_in_cents() > 0:
                refund_user_money()
            break
        # Allows users to reset /cancel the continuing transactions. It restarts the transaction
        elif option == "6":
            if cart.get_cart():
                cart.reset_cart()
                print("Your cart has been cleared")
                if user_payment.current_coin_amount_in_cents() > 0:
                    refund_user_money()
                new_transaction(True)
                break
            else:
                print("\nYou do NOT have any ITEMS in your CART")
        else:
            print("Invalid choice")


def main_menu_list():
    print("\nYou are in the Main Menu!")
    print("Please choose one of the following options")
    print("1. New Transaction")
    print("2. List of Products")
    print("3. Change Machine Status (ADMIN)")
    print("4. Statistical Report (ADMIN)")
    print("5. Reset System (ADMIN)")
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
            cart.reset_cart()
            print(cart)
            new_transaction(True)
            break
        else:
            print("unknown input, please enter (y/n)")


def change_machine_status():
    while True:
        print("\nChanging Machine Status Menu\n")
        print("Are you sure you would like to change the current machine status of", machine.get_machine_status(),"?")
        option = input("please answer with (y/n)")
        if option.lower() == "y":
            if machine.get_machine_status() == "working":
                machine.set_maintenance_status()
            elif machine.get_machine_status() == "maintenance":
                machine.set_working_status()
            print("Your Machine status has now been changed...")
            break
        elif option.lower() == "n":
            print("returning you to Main Menu")
            break
        else:
            print("""Invalid choice, please answer with the character "y" or "n" only""")


def provide_statistical_report():
    transaction_history = transaction.get_transaction()

    print("\nPurchase History")
    for transaction_id in transaction_history:
        print("\nTransaction ID:", transaction_id)
        for key_name in transaction_history[transaction_id]:
            if key_name == "items":
                result_string = ",".join(transaction_history[transaction_id][key_name])
                print("Items Purchased:", result_string)
            elif key_name == "payment":
                print("Transaction Amount: $" + str((int(transaction_history[transaction_id][key_name])/100)))
            elif key_name == "date":
                print("Date Purchased:", transaction_history[transaction_id][key_name])


def reset_operation_for_vending_machine():
    while True:
        print("\nWe are about to reset your machine.")
        output = input("Are you sure you would like to reset? (y/n): ")
        if output == "y":
            items.reset_items_to_default()
            machine.reset_items_to_default()
            ingredient.reset_items_to_default()
            cart.reset_cart()
            print("Resetting...")
            for i in tqdm(range(10)):
                time.sleep(1)
            break
        elif output == "n":
            print("Returning you back to Main Menu...")
            break
        else:
            print("Invalid input")


def display_main_menu():
    menu_over = False

    while not menu_over:
        print("\nMachine Status:", machine.get_machine_status().capitalize())
        main_menu_list()
        choice = input("Select an Option: ")

        if str(choice).lower() == "1":
            if machine.get_machine_status() == "working":
                # Need to check if the cart has items. If so, ask the user if they want to restart. Else keep the cart
                if cart.get_cart():
                    # if cart has items, go inside the function and ask what they want to do with the transaction
                    cancel_transaction_or_keep_previous_transaction()
                else:
                    # Start Transaction
                    new_transaction(True)
            else:
                print("The System is currently Under maintenance.")
                print("Please contact your ADMIN for further information.")
        elif str(choice).lower() == "2":
            # Display List
            items.display_list_of_products()
        elif str(choice).lower() == "3" or str(choice).lower() == "4" or str(choice).lower() == "5":
            password_input = input("Admin Password (123): ")
            # Continue depending on the variable "Choice"
            if password_input == "123":
                if str(choice).lower() == "4":
                    provide_statistical_report()
                elif str(choice).lower() == "3":
                    change_machine_status()
                elif str(choice).lower() == "5":
                    reset_operation_for_vending_machine()
            else:
                print("Wrong Password")
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
