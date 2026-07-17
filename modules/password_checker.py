"""
============================================================
Cyber Recon Toolkit
Module  : Password Strength Checker
Version : 2.0
Author  : David Didomi
============================================================
"""

import re
import os
from datetime import datetime
from time import time

# ============================================
# CYBER RECON TOOLKIT - PASSWORD CHECKER
# ============================================

print("\n" + "=" * 60)
print("      CYBER RECON TOOLKIT - PASSWORD CHECKER")
print("=" * 60)

password = input("Enter a password: ")

start_time = time()

score = 0
feedback = []

# Common passwords
common_passwords = [
    "123456",
    "password",
    "qwerty",
    "abc123",
    "admin",
    "letmein",
    "welcome",
    "password123"
]

# Create reports folder
os.makedirs("reports", exist_ok=True)

report_file = "reports/password_report.txt"
# -------------------------------
# Check if password is common
# -------------------------------

if password.lower() in common_passwords:

    print("\n❌ This is a very common password.")
    print("Please choose a stronger password.")

    with open(report_file, "w") as report:

        report.write("PASSWORD ANALYSIS REPORT\n")
        report.write("=" * 50 + "\n")
        report.write(f"Date : {datetime.now()}\n\n")
        report.write("Result : Common Password Detected\n")

    print(f"\n[+] Report saved to: {report_file}")
    exit()

# -------------------------------
# Password Checks
# -------------------------------

length = len(password)

has_upper = bool(re.search(r"[A-Z]", password))
has_lower = bool(re.search(r"[a-z]", password))
has_number = bool(re.search(r"[0-9]", password))
has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
has_space = bool(re.search(r"\s", password))
repeated = bool(re.search(r"(.)\1\1", password))

# Length
if length >= 12:
    score += 2
elif length >= 8:
    score += 1
else:
    feedback.append("Use at least 12 characters.")

# Uppercase
if has_upper:
    score += 2
else:
    feedback.append("Add uppercase letters.")

# Lowercase
if has_lower:
    score += 2
else:
    feedback.append("Add lowercase letters.")

# Numbers
if has_number:
    score += 2
else:
    feedback.append("Add numbers.")

# Special Characters
if has_special:
    score += 2
else:
    feedback.append("Add special characters.")

# Spaces
if has_space:
    feedback.append("Avoid spaces in passwords.")

# Repeated Characters
if repeated:
    feedback.append("Avoid repeated characters (e.g. AAA or 111).")

# -------------------------------
# Password Strength
# -------------------------------

if score <= 4:
    strength = "WEAK ❌"

elif score <= 7:
    strength = "MEDIUM ⚠️"

else:
    strength = "STRONG ✅"

elapsed = round(time() - start_time, 2)

# -------------------------------
# Display Results
# -------------------------------

print("\n" + "=" * 60)
print("PASSWORD ANALYSIS")
print("=" * 60)

print(f"Length              : {length}")
print(f"Uppercase           : {'Yes' if has_upper else 'No'}")
print(f"Lowercase           : {'Yes' if has_lower else 'No'}")
print(f"Numbers             : {'Yes' if has_number else 'No'}")
print(f"Special Characters  : {'Yes' if has_special else 'No'}")
print(f"Contains Spaces     : {'Yes' if has_space else 'No'}")
print(f"Repeated Characters : {'Yes' if repeated else 'No'}")

print("\n--------------------------------------------")
print(f"Score               : {score}/10")
print(f"Strength            : {strength}")
print("--------------------------------------------")

# Recommendations

if strength.startswith("STRONG"):

    print("\nRecommended For:")
    print("✔ Email Accounts")
    print("✔ Social Media")
    print("✔ Banking")
    print("✔ Administrator Accounts")

elif strength.startswith("MEDIUM"):

    print("\nSuitable For:")
    print("✔ Normal Accounts")
    print("⚠ Avoid using for banking.")

else:

    print("\nNot recommended for important accounts.")

# Suggestions

if feedback:

    print("\nSuggestions:")

    for tip in feedback:
        print(f"- {tip}")

else:

    print("\nExcellent password!")

# -------------------------------
# Save Report
# -------------------------------

with open(report_file, "a") as report:

    report.write("=" * 60 + "\n")
    report.write("PASSWORD ANALYSIS REPORT\n")
    report.write("=" * 60 + "\n\n")
    report.write("\n")
    report.write("=" * 60 + "\n")
    report.write(f"Analysis Date : {datetime.now()}\n")
    report.write("=" * 60 + "\n")
    report.write(f"Date                 : {datetime.now()}\n")
    report.write(f"Password Length      : {length}\n")
    report.write(f"Uppercase            : {has_upper}\n")
    report.write(f"Lowercase            : {has_lower}\n")
    report.write(f"Numbers              : {has_number}\n")
    report.write(f"Special Characters   : {has_special}\n")
    report.write(f"Contains Spaces      : {has_space}\n")
    report.write(f"Repeated Characters  : {repeated}\n")
    report.write(f"Score                : {score}/10\n")
    report.write(f"Strength             : {strength}\n")
    report.write(f"Analysis Time        : {elapsed} seconds\n")

print(f"\n[+] Report saved to: {report_file}")
print("=" * 60)