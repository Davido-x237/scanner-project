import re

print("=== PASSWORD STRENGTH CHECKER ===\n")

password = input("Enter a password: ")
import re

print("=== ADVANCED PASSWORD CHECKER ===\n")

password = input("Enter a password: ")

score = 0
feedback = []

common_passwords = ["123456", "password", "qwerty", "abc123", "admin"]

# Check common passwords
if password.lower() in common_passwords:
    print("\n❌ This is a very common password!")
    exit()

# Length
if len(password) >= 8:
    score += 2
else:
    feedback.append("Use at least 8 characters")

# Uppercase
if re.search(r"[A-Z]", password):
    score += 2
else:
    feedback.append("Add uppercase letters")

# Lowercase
if re.search(r"[a-z]", password):
    score += 2
else:
    feedback.append("Add lowercase letters")

# Numbers
if re.search(r"[0-9]", password):
    score += 2
else:
    feedback.append("Add numbers")

# Special characters
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 2
else:
    feedback.append("Add special characters")

# Final Score
print(f"\nScore: {score}/10")

if score <= 4:
    print("Strength: Weak ❌")
elif score <= 7:
    print("Strength: Medium ⚠️")
else:
    print("Strength: Strong ✅")

# Feedback
if feedback:
    print("\nSuggestions to improve:")
    for tip in feedback:
        print(f"- {tip}")
else:
    print("\nGreat password! 🔥")
