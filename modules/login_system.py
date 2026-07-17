"""
============================================================
Cyber Recon Toolkit
Module  : Secure Login System
Version : 2.0
Author  : David Didomi
============================================================
"""

import hashlib
import os
import re
from datetime import datetime

# ==========================================================
# CONFIGURATION
# ==========================================================

VERSION = "2.0"

USERS_FILE = "data/users.txt"
REPORT_FILE = "reports/login_report.txt"
LOG_FILE = "logs/login.log"

# ==========================================================
# INITIALIZATION
# ==========================================================

def ensure_directories():
    """
    Create project folders if they do not already exist.
    """

    os.makedirs("data", exist_ok=True)
    os.makedirs("reports", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

    if not os.path.exists(USERS_FILE):
        open(USERS_FILE, "w").close()


# ==========================================================
# USER INTERFACE
# ==========================================================

def print_banner():

    print("\n" + "=" * 60)
    print("        CYBER RECON TOOLKIT")
    print("           Secure Login System")
    print(f"             Version {VERSION}")
    print("=" * 60)


# ==========================================================
# SECURITY
# ==========================================================

def hash_password(password):
    """
    Return the SHA-256 hash of a password.
    """

    return hashlib.sha256(password.encode()).hexdigest()


# ==========================================================
# VALIDATION
# ==========================================================

def validate_username(username):
    """
    Validate username.
    Rules:
        - 4 to 20 characters
        - Letters, numbers and underscore only
    """

    if len(username) < 4:
        print("❌ Username must contain at least 4 characters.")
        return False

    if len(username) > 20:
        print("❌ Username cannot exceed 20 characters.")
        return False

    if not re.fullmatch(r"[A-Za-z0-9_]+", username):
        print("❌ Username can only contain letters, numbers and underscores.")
        return False

    return True


def validate_password(password):
    """
    Validate password strength.
    """

    feedback = []

    if len(password) < 8:
        feedback.append("- Minimum length is 8 characters.")

    if not re.search(r"[A-Z]", password):
        feedback.append("- Add an uppercase letter.")

    if not re.search(r"[a-z]", password):
        feedback.append("- Add a lowercase letter.")

    if not re.search(r"[0-9]", password):
        feedback.append("- Add a number.")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("- Add a special character.")

    if feedback:

        print("\nPassword is not strong enough:\n")

        for item in feedback:
            print(item)

        return False

    return True


# ==========================================================
# FILE MANAGEMENT
# ==========================================================

def load_users():
    """
    Load every user from users.txt
    Return a dictionary.
    """

    users = {}

    with open(USERS_FILE, "r") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            username, password_hash = line.split(":")

            users[username] = password_hash

    return users


def save_user(username, password_hash):
    """
    Save a new user.
    """

    with open(USERS_FILE, "a") as file:

        file.write(f"{username}:{password_hash}\n")


def user_exists(username):
    """
    Check whether a username already exists.
    """

    users = load_users()

    return username in users


# ==========================================================
# REPORTING
# ==========================================================

def write_report(operation, username, status):

    with open(REPORT_FILE, "a") as report:

        report.write("\n")
        report.write("=" * 60 + "\n")
        report.write("LOGIN SYSTEM REPORT\n")
        report.write("=" * 60 + "\n")
        report.write(f"Date      : {datetime.now()}\n")
        report.write(f"Operation : {operation}\n")
        report.write(f"Username  : {username}\n")
        report.write(f"Status    : {status}\n")


# ==========================================================
# LOGGING
# ==========================================================

def write_log(message):

    with open(LOG_FILE, "a") as log:

        log.write(
            f"[{datetime.now()}] {message}\n"
        )

# ==========================================================
# REGISTRATION
# ==========================================================

def register_user():

    print("\n--- USER REGISTRATION ---")

    username = input("Enter username: ").strip()

    if not validate_username(username):
        return

    if user_exists(username):
        print("\n❌ Username already exists.")
        write_log(f"REGISTER FAILED - Username '{username}' already exists.")
        write_report("REGISTER", username, "FAILED")
        return

    password = input("Enter password: ")

    if not validate_password(password):
        write_log(f"REGISTER FAILED - Weak password for '{username}'.")
        write_report("REGISTER", username, "FAILED")
        return

    password_hash = hash_password(password)

    save_user(username, password_hash)

    print("\n✅ Registration successful!")

    write_log(f"REGISTER SUCCESS - User '{username}' created.")
    write_report("REGISTER", username, "SUCCESS")


# ==========================================================
# LOGIN
# ==========================================================

def login_user():

    print("\n--- USER LOGIN ---")

    username = input("Username: ").strip()

    password = input("Password: ")

    users = load_users()

    if username not in users:

        print("\n❌ User does not exist.")

        write_log(f"LOGIN FAILED - Unknown user '{username}'.")
        write_report("LOGIN", username, "FAILED")

        return

    password_hash = hash_password(password)

    if users[username] == password_hash:

        print("\n✅ Login successful!")

        write_log(f"LOGIN SUCCESS - User '{username}'.")
        write_report("LOGIN", username, "SUCCESS")

    else:

        print("\n❌ Incorrect password.")

        write_log(f"LOGIN FAILED - Wrong password for '{username}'.")
        write_report("LOGIN", username, "FAILED")


# ==========================================================
# MENU
# ==========================================================

def display_menu():

    print("\n")
    print("1. Register User")
    print("2. Login")
    print("3. View Registered Users")
    print("0. Exit")


# ==========================================================
# OPTIONAL ADMIN FUNCTION
# ==========================================================

def view_users():

    users = load_users()

    if not users:

        print("\nNo registered users.")

        return

    print("\nRegistered Users")
    print("-" * 40)

    for username in users:

        print(username)


# ==========================================================
# MAIN
# ==========================================================

def main():

    ensure_directories()

    while True:

        print_banner()

        display_menu()

        choice = input("\nSelect an option: ").strip()

        if choice == "1":

            register_user()

        elif choice == "2":

            login_user()

        elif choice == "3":

            view_users()

        elif choice == "0":

            print("\nThank you for using the Cyber Recon Toolkit.")
            break

        else:

            print("\n❌ Invalid option.")


# ==========================================================
# PROGRAM ENTRY
# ==========================================================

if __name__ == "__main__":

    main()