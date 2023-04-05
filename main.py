# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def main_menu_list():
    print("Welcome to the Vending Machine!")
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
    print("Welcome to Monash University Vending Machine")
    display_main_menu()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    startup()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
