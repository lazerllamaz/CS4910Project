import tkinter
import customtkinter


# System settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

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







# Run app
app.mainloop()