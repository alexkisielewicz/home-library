import constants
from scripts import functions
from utils.utils import clear_terminal


def logo():
    print("""
    ██   ██  ██████  ███    ███ ███████     ██      ██ ██████  ██████   █████  ██████  ██    ██ 
    ██   ██ ██    ██ ████  ████ ██          ██      ██ ██   ██ ██   ██ ██   ██ ██   ██  ██  ██  
    ███████ ██    ██ ██ ████ ██ █████       ██      ██ ██████  ██████  ███████ ██████    ████   
    ██   ██ ██    ██ ██  ██  ██ ██          ██      ██ ██   ██ ██   ██ ██   ██ ██   ██    ██    
    ██   ██  ██████  ██      ██ ███████     ███████ ██ ██████  ██   ██ ██   ██ ██   ██    ██                                                                           
    """)
    print(f"Welcome to {constants.APP} app, you can manage all your books here. Please select option 1-7 to continue.")


def menu():
    print("""
    1. Add book
    2. Edit book
    3. Remove book
    4. View all books
    5. Change sorting method
    6. Show #book details
    7. Quit
    """)


def show_menu():
    while True:
        menu()
        user_choice = input("Please select a number from 1 to 5 to continue: ")
        if user_choice == "1":
            clear_terminal()
            functions.add_book()
        elif user_choice == "2":
            clear_terminal()
            functions.edit_book()
        elif user_choice == "3":
            clear_terminal()
            functions.remove_book()
        elif user_choice == "4":
            clear_terminal()
            functions.show_all_books()
        elif user_choice == "5":
            clear_terminal()
            functions.change_sorting_method()
        elif user_choice == "6":
            clear_terminal()
            functions.show_book_details()
        elif user_choice == "7":
            clear_terminal()
            functions.quit_app()
            break
        else:
            print("No such option. Please select a number from 1 to 5.")
