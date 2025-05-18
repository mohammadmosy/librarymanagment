import json
import os
import objects

FILENAME = "sample.json"

# Checking for file existence and creating the initial file if it does not exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        json.dump([], f)

# Loading users from file
def load_users():
    with open(FILENAME, "r") as f:
        return json.load(f)

# Save users to file
def save_users(users):
    with open(FILENAME, "w") as f:
        json.dump(users, f, indent=4)

# User login
def login():
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    users = load_users()

    for user in users:
        if user["name"] == name and user["password"] == password:
            print("Login successful!")
            objects.list_books()
            return
    print("Invalid username or password.")

# Add new user
def add_user():
    name = input("New user's name: ")
    password = input("New user's password: ")
    users = load_users()

    # Checking for duplicate names
    for user in users:
        if user["name"] == name:
            print("User already exists!")
            return

    users.append({"name": name, "password": password})
    save_users(users)
    print("User added successfully.")

# Delete user
def delete_user():
    name = input("Enter the username to delete: ")
    users = load_users()

    updated_users = [user for user in users if user["name"] != name]
    if len(updated_users) == len(users):
        print("User not found.")
    else:
        save_users(updated_users)
        print("User deleted successfully.")

# Main menu
def main():
    while True:

        choice = input("1. Login\n2. Add user\n3. Delete user\n4. Exit\n choice:>")
        match choice:
            case"1":
                login()
            case"2":
                add_user()
            case"3":
                delete_user()
      



