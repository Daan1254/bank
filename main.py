import json

def load_balance():
    try:
        with open('balance.json', 'r') as file:
            data = json.load(file)
            return data['balance']
    except FileNotFoundError:
        return 0

def save_balance(balance):
    data = {'balance': balance}
    with open('balance.json', 'w') as file:
        json.dump(data, file)

def deposit(amount):
    balance = load_balance()
    balance += amount
    save_balance(balance)
    print(f"Successfully deposited ${amount}. New balance: ${balance}")

def withdraw(amount):
    balance = load_balance()
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        save_balance(balance)
        print(f"Successfully withdrew ${amount}. New balance: ${balance}")

def show_menu():
    while True:
        print("==== Banking App Menu ====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            amount = float(input("Enter the deposit amount: $"))
            deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the withdrawal amount: $"))
            withdraw(amount)
        elif choice == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == '__main__':
    show_menu()