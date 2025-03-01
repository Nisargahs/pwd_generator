import random
import tkinter as tk
from tkinter import messagebox


# Function to generate password
def generate_password():
    
    try:
        passlen = int(length_entry.get())  # Get password length from input field
        if passlen < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4!")
            return

        # Character sets
        alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        special_chars = "@#$%^&*!?"

        char_pool = ""

        if alphabets_var.get():
            char_pool += alphabets
        if numbers_var.get():
            char_pool += numbers
        if special_chars_var.get():
            char_pool += special_chars

        if not char_pool:
            messagebox.showwarning("Warning", "Select at least one option!")
            return

        password = "".join(random.sample(char_pool, passlen))
        password_label.config(text=f"Generated Password: {password}")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number for password length!")


# Tkinter GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.config(bg="lightgray")

# Label for password length
tk.Label(root, text="Enter Password Length:", bg="lightgray").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack()

# Checkboxes for options
alphabets_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=False)
special_chars_var = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Include Alphabets", variable=alphabets_var, bg="lightgray").pack()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var, bg="lightgray").pack()
tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var, bg="lightgray").pack()

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white").pack(pady=10)

# Label to display password
password_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="blue", bg="lightgray")
password_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()