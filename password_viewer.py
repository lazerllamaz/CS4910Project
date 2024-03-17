import sqlite3
import encryption_manager
import customtkinter as ctk
import sys

def print_passwords():
    # Connect to the database
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()

    # Retrieve website-password pairs from the database
    cursor.execute("SELECT website, password FROM passwords")
    rows = cursor.fetchall()

    # Print the website-password pairs
    for row in rows:
        website, password = row
        print("Website:", website)
        print("Encrypted Password:", password)
        password = encryption_manager.decrypt_password(password)
        print("Unencrypted Password:", password)
        print()  # Add an empty line between pairs

    # Close the cursor and connection
    cursor.close()
    conn.close()



def print_passwords_gui():
    # Connect to the database
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()

    # Retrieve website-password pairs from the database
    cursor.execute("SELECT website, password FROM passwords")
    rows = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Creating the GUI window
    window = ctk.CTk()
    window.title("Password Manager")
    window.geometry("400x300")

    
    def on_close():
        # Handle any pending operations before closing
        window.update_idletasks()
        window.destroy()
        # Properly terminate the application
        sys.exit()

    # Bind the close event to the on_close function
    window.protocol("WM_DELETE_WINDOW", on_close)

    # Creating a frame that will contain the canvas and scrollbar
    container = ctk.CTkFrame(window)
    container.pack(fill="both", expand=True)

    # Canvas for scrolling
    canvas = ctk.CTkCanvas(container)
    canvas.pack(side="left", fill="both", expand=True)

    # Scrollbar
    scrollbar = ctk.CTkScrollbar(container, command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure canvas scrolling
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Frame for content
    content_frame = ctk.CTkFrame(canvas)
    canvas.create_window((0, 0), window=content_frame, anchor="nw", width=window.winfo_width())

    # Displaying the passwords
    for row in rows:
        website, encrypted_password = row
        decrypted_password = encryption_manager.decrypt_password(encrypted_password)

        website_label = ctk.CTkLabel(content_frame, text=f"Website: {website}")
        website_label.pack(pady=5)

        password_label = ctk.CTkLabel(content_frame, text=f"Password: {encrypted_password}")
        password_label.pack(pady=5)

        password_label = ctk.CTkLabel(content_frame, text=f"Password: {decrypted_password}")
        password_label.pack(pady=5)

    try:
        window.mainloop()
    except Exception as e:
        print("An error occurred:", e)