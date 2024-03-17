import customtkinter
import database_manager
from tkinter import messagebox
from cryptography.fernet import Fernet
import hashlib
import os
import password_viewer
import encryption_manager

class PasswordManagerApp:
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.geometry("720x480")
        self.app.title("Password Manager")

        # UI elements
        self.title = customtkinter.CTkLabel(self.app, text="Type a password")
        self.title.pack(padx=10, pady=10)


        # Website entry
        self.website_var = customtkinter.StringVar()
        self.website_label = customtkinter.CTkLabel(self.app, text="Website:")
        self.website_label.pack(padx=10, pady=5)
        self.website_entry = customtkinter.CTkEntry(self.app, width=350, textvariable=self.website_var)
        self.website_entry.pack()

        # Password entry
        self.password_var = customtkinter.StringVar()
        self.password_label = customtkinter.CTkLabel(self.app, text="Password:")
        self.password_label.pack(padx=10, pady=5)
        self.password_entry = customtkinter.CTkEntry(self.app, width=350, textvariable=self.password_var, show="*")
        self.password_entry.pack()

        self.save_button = customtkinter.CTkButton(self.app, text="Save Password", command=self.save_password)
        self.save_button.pack(pady=10)

        self.view_passwords_button = customtkinter.CTkButton(self.app, text="View Passwords", command=self.view_passwords)
        self.view_passwords_button.pack()
        

    def save_password(self):
        website = self.website_var.get()
        password = self.password_var.get()
        database_manager.save_password(website, password)
        messagebox.showinfo("Success", "Password saved successfully!")


    def derive_key(self, password, salt=None):
        if salt is None:
            salt = os.urandom(16)  # Generate a random salt
        key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000) # Generate a key
        return key, salt
    

    def view_passwords(self):
        # Prompt the user for their password
        password_window = customtkinter.CTk()
        password_window.title("Enter Password")
        password_label = customtkinter.CTkLabel(password_window, text="Enter your password:")
        password_label.pack()
        password_entry = customtkinter.CTkEntry(password_window, show="*")  # Mask the password
        password_entry.pack()
        
        def submit_password():
            password = password_entry.get()
            key, salt = self.derive_key(password)
            print("Derived key:", key)
            print("Salt:", salt)
            password_window.destroy()

        submit_button = customtkinter.CTkButton(password_window, text="Submit", command=submit_password)
        submit_button.pack()

        password_viewer.print_passwords()

        password_window.mainloop()
    

    def run(self):
        self.app.mainloop()
