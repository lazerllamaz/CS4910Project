import tkinter
import customtkinter
import sqlite3
from tkinter import messagebox

# System settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

# Function to save password securely
def save_password():
    website = website_var.get()
    password = password_var.get()
    
    # Connect to the SQLite database
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()

    # Create a table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS passwords
                 (website TEXT, password TEXT)''')

    # Insert the new password into the table
    c.execute("INSERT INTO passwords (website, password) VALUES (?, ?)", (website, password))
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Password saved successfully!")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Password Manager")

# UI elements
title = customtkinter.CTkLabel(app, text="Type a password")
title.pack(padx=10, pady=10)

# Website input
website_var = tkinter.StringVar()
website_label = customtkinter.CTkLabel(app, text="Website:")
website_label.pack(padx=10, pady=5)
website_entry = customtkinter.CTkEntry(app, width=50, textvariable=website_var)
website_entry.pack()

# Password input
password_var = tkinter.StringVar()
password_label = customtkinter.CTkLabel(app, text="Password:")
password_label.pack(padx=10, pady=5)
password_entry = customtkinter.CTkEntry(app, width=50, textvariable=password_var)
password_entry.pack()

# Save button
save_button = customtkinter.CTkButton(app, text="Save Password", command=save_password)
save_button.pack(pady=10)

# Run app
app.mainloop()
