import tkinter
import customtkinter
from tkinter import messagebox

# System settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

# Function to save password securely
def save_password():
    password = password_var.get()
    # You should implement your secure saving mechanism here
    messagebox.showinfo("Success", "Password saved successfully!")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Password Manager")

# UI elements
title = customtkinter.CTkLabel(app, text="Type a password")
title.pack(padx=10, pady=10)

# Password input
password_var = tkinter.StringVar()
password = customtkinter.CTkEntry(app, width=350, height=40, textvariable=password_var)
password.pack()

# Save button
save_button = customtkinter.CTkButton(app, text="Save Password", command=save_password)
save_button.pack(pady=10)

# Run app
app.mainloop()
