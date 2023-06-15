import os
import json


# add variable to store the data
data = []
current_user = None


def init_data():
    data_dir = "./data"
    json_file = "bank_data.json"

    # Create the data directory if it doesn't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Create the JSON file if it doesn't exist
    file_path = os.path.join(data_dir, json_file)
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump([], file)


def check_pin(pin: int):
    global data, current_user
    data_dir = "./data"
    json_file = "bank_data.json"
    file_path = os.path.join(data_dir, json_file)

    if not os.path.exists(file_path):
        print("Something went wrong. Please try again later.")
        quit()

    with open(file_path, "r") as file:
        data = json.load(file)

    for i in range(len(data)):
        if data[i]["pin"] == pin:
            current_user = data[i]
            print(current_user)
            return
    print("Wrong pin")


def enter_pin():
    while True:
        print("Please enter your pin\n")
        pin = input()
        if not pin.isdigit():
            print("Please enter a valid pin")
            return
        int(pin)
        if len(pin) != 4:
            print("Please enter a valid pin")
            return
        else:
            check_pin(pin)


def main():
    init_data()
    print("Welcome to the bank!\n")
    enter_pin()


if __name__ == "__main__":
    main()


