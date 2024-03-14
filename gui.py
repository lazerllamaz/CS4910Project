import customtkinter
import database_manager
from tkinter import messagebox

class PasswordManagerApp:
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.geometry("720x480")
        self.app.title("Password Manager")

        # UI elements
        self.title = customtkinter.CTkLabel(self.app, text="Type a password")
        self.title.pack(padx=10, pady=10)

        self.website_var = customtkinter.StringVar()
        self.website_label = customtkinter.CTkLabel(self.app, text="Website:")
        self.website_label.pack(padx=10, pady=5)
        self.website_entry = customtkinter.CTkEntry(self.app, width=350, textvariable=self.website_var)
        self.website_entry.pack()

        self.password_var = customtkinter.StringVar()
        self.password_label = customtkinter.CTkLabel(self.app, text="Password:")
        self.password_label.pack(padx=10, pady=5)
        self.password_entry = customtkinter.CTkEntry(self.app, width=350, textvariable=self.password_var)
        self.password_entry.pack()

        self.save_button = customtkinter.CTkButton(self.app, text="Save Password", command=self.save_password)
        self.save_button.pack(pady=10)
        

    def save_password(self):
        website = self.website_var.get()
        password = self.password_var.get()
        database_manager.save_password(website, password)
        messagebox.showinfo("Success", "Password saved successfully!")

    def run(self):
        self.app.mainloop()
