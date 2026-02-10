import tkinter as tk
from tkinter import messagebox, scrolledtext
import re
import os

# Common passwords
common_passwords = [
    "123456", "password", "123456789", "qwerty",
    "abc123", "password123", "admin", "letmein"
]

REPORT_FILE = "password_report.txt"

# ---------------- Password Checking Logic ----------------

def check_password():
    password = entry_password.get()
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("At least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special character")

    is_common = password.lower() in common_passwords

    if score <= 2:
        strength = "WEAK ❌"
        crack_time = "Few seconds"
    elif score <= 4:
        strength = "MEDIUM ⚠"
        crack_time = "Few hours to days"
    else:
        strength = "STRONG ✅"
        crack_time = "Years"

    result = f"Strength: {strength}\nCrack Time: {crack_time}\n"

    if is_common:
        result += "⚠ Common password detected!\n"

    if feedback:
        result += "\nSuggestions:\n"
        for tip in feedback:
            result += f"- {tip}\n"

    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, result)

    save_report(result)


def save_report(text):
    with open(REPORT_FILE, "a", encoding="utf-8") as file:
        file.write(text + "\n-----------------\n")


# ---------------- Admin Panel ----------------

def open_admin():
    admin_window = tk.Toplevel(root)
    admin_window.title("Admin Panel - Reports")
    admin_window.geometry("400x300")

    report_box = scrolledtext.ScrolledText(admin_window, width=45, height=15)
    report_box.pack(padx=10, pady=10)

    if os.path.exists(REPORT_FILE):
        with open(REPORT_FILE, "r", encoding="utf-8") as file:
            report_box.insert(tk.END, file.read())
    else:
        report_box.insert(tk.END, "No reports found.")


# ---------------- Main UI ----------------

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("420x420")

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=5)

entry_password = tk.Entry(root, width=30, show="*", font=("Arial", 12))
entry_password.pack(pady=5)

tk.Button(root, text="Check Strength", command=check_password, bg="#4CAF50", fg="white").pack(pady=10)

output_box = scrolledtext.ScrolledText(root, width=45, height=10)
output_box.pack(pady=5)

tk.Button(root, text="Admin Panel", command=open_admin, bg="#2196F3", fg="white").pack(pady=10)

root.mainloop()
