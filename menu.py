from main import enter_pin

menu_data = ["1. Enter pin", "2. Create account", "3. Exit"]


def main_menu():
    global menu_data
    while True:
        for option in menu_data:
            print(option)
        choice = input()
        if choice == "1":
            enter_pin()
        elif choice == "2":
            print("Create account")
        elif choice == "3":
            print("Goodbye!")
            quit()
        else:
            print("Please enter a valid option")