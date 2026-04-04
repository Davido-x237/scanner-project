import re

print("=== PASSWORD STRENGTH CHECKER ===\n")

password = input("Enter a password: ")

score = 0

# Length check
if len(password) >= 8:
    score += 1

# Uppercase
if re.search(r"[A-Z]", password):
    score += 1

# Lowercase
if re.search(r"[a-z]", password):
    score += 1

# Numbers
if re.search(r"[0-9]", password):
    score += 1

# Special characters
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1

# Result
print("\nPassword strength:")

if score <= 2:
    print("Weak ❌")
elif score == 3 or score == 4:
    print("Medium ⚠️")
else:
    print("Strong ✅")
