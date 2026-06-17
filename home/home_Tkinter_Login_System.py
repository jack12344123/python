import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "../home.users.json"


# Load saved users
def load_users():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


# Save users
def save_users(users):
    with open(FILE_NAME, "w") as file:
        json.dump(users, file)


# Register new user
def register():
    username = username_entry.get()
    password = password_entry.get()

    users = load_users()

    if username in users:
        messagebox.showerror("Error", "Username already exists")
    else:
        users[username] = password
        save_users(users)
        messagebox.showinfo("Success", "User registered successfully")


# Login existing user
def login():
    username = username_entry.get()
    password = password_entry.get()

    users = load_users()

    if username in users and users[username] == password:
        messagebox.showinfo("Success", "Login successful")
    else:
        messagebox.showerror("Error", "Invalid username or password")


# Window
window = tk.Tk()
window.title("Login System")
window.geometry("300x200")

tk.Label(window, text="Username").pack(pady=5)
username_entry = tk.Entry(window)
username_entry.pack()

tk.Label(window, text="Password").pack(pady=5)
password_entry = tk.Entry(window, show="*")
password_entry.pack()

tk.Button(window, text="Register", command=register).pack(pady=10)
tk.Button(window, text="Login", command=login).pack()

window.mainloop()