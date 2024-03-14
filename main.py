import customtkinter
import gui
import sys
import database_manager

def main():
    if len(sys.argv) != 2:
        print("Available commands: reset")
        return
        
    command = sys.argv[1]
        
    if command == "reset":
        database_manager.reset_database()
    else:
        print("Invalid command. Available commands: reset")

if __name__ == "__main__":
    # System settings
    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("blue")

    # Create and run the GUI
    app = gui.PasswordManagerApp()
    app.run()

    main()