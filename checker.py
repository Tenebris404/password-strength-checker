import re

# List of common passwords
common_passwords = [
    "123456", "password", "123456789", "qwerty",
    "abc123", "password123", "admin", "letmein"
]

password = input("Enter your password: ")

score = 0
feedback = []

# Rule 1: Length
if len(password) >= 8:
    score += 1
else:
    feedback.append("Password should be at least 8 characters long")

# Rule 2: Uppercase
if re.search(r"[A-Z]", password):
    score += 1
else:
    feedback.append("Add at least one uppercase letter")

# Rule 3: Lowercase
if re.search(r"[a-z]", password):
    score += 1
else:
    feedback.append("Add at least one lowercase letter")

# Rule 4: Number
if re.search(r"[0-9]", password):
    score += 1
else:
    feedback.append("Add at least one number")

# Rule 5: Special character
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
else:
    feedback.append("Add at least one special character")

# Common password check
is_common = password.lower() in common_passwords

# Strength result
if score <= 2:
    strength = "WEAK ❌"
    crack_time = "Few seconds"
elif score <= 4:
    strength = "MEDIUM ⚠"
    crack_time = "Few hours to days"
else:
    strength = "STRONG ✅"
    crack_time = "Years (basic estimation)"

# Output
print("\nPassword Strength:", strength)
print("Estimated Crack Time:", crack_time)

if is_common:
    print("⚠ Warning: This password is commonly used!")

if feedback:
    print("\nSuggestions to improve:")
    for tip in feedback:
        print("-", tip)

# Save result
save = input("\nDo you want to save this result? (y/n): ").lower()
if save == "y":
    with open("password_report.txt", "w") as file:
        file.write(f"Password Strength: {strength}\n")
        file.write(f"Estimated Crack Time: {crack_time}\n")
        if is_common:
            file.write("Warning: Common password detected\n")
        if feedback:
            file.write("Suggestions:\n")
            for tip in feedback:
                file.write(f"- {tip}\n")
    print("Result saved to password_report.txt")

