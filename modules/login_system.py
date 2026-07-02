import os
import hashlib

FILE = "users.txt"

if not os.path.exists(FILE):
    open(FILE, "w").close()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed = hash_password(password)

    with open(FILE, "r") as f:
        users = f.readlines()

    for user in users:
        if username in user:
            print("User already exists!")
            return

    with open(FILE, "a") as f:
        f.write(f"{username}:{hashed}\n")

    print("Registration successful! 🔐")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed = hash_password(password)

    with open(FILE, "r") as f:
        users = f.readlines()

    for user in users:
        stored_user, stored_pass = user.strip().split(":")
        if username == stored_user and hashed == stored_pass:
            print("Login successful! ✅")
            return

    print("Invalid credentials ❌")


def main():
    while True:
        print("\n=== SECURE LOGIN SYSTEM ===")
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
