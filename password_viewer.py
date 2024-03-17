import sqlite3
import encryption_manager

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
        print("Password Hash:", password)
        print()  # Add an empty line between pairs

    # Close the cursor and connection
    cursor.close()
    conn.close()