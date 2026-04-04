import os

FILE = "users.txt"

# Ensure file exists
if not os.path.exists(FILE):
    open(FILE, "w").close()


def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(FILE, "r") as f:
        users = f.readlines()

    for user in users:
        if username in user:
            print("User already exists!")
            return

    with open(FILE, "a") as f:
        f.write(f"{username}:{password}\n")

    print("Registration successful!")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(FILE, "r") as f:
        users = f.readlines()

    for user in users:
        stored_user, stored_pass = user.strip().split(":")
        if username == stored_user and password == stored_pass:
            print("Login successful! ✅")
            return

    print("Invalid credentials ❌")


def main():
    while True:
        print("\n=== LOGIN SYSTEM ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
