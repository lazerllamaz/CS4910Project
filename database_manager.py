import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database"""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None


def create_table(conn):
    """Create the passwords table if it doesn't exist"""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            website TEXT NOT NULL,
            password TEXT NOT NULL
            )
        ''')
        conn.commit()
        cursor.close()
    except sqlite3.Error as e:
        print(e)


def save_password(website, password):
    """Save a password to the database"""
    conn = create_connection('passwords.db')
    create_table(conn)
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO passwords (website, password) VALUES (?, ?)", (website, password))
            conn.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

def reset_database():
    """Reset the database by dropping and recreating the passwords table"""
    conn = create_connection('passwords.db')
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS passwords")
            create_table(conn)
            print("Database reset successful!")
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

# Add more database functions as needed
