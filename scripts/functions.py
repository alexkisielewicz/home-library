import constants
import app_menu as menu
from prettytable import PrettyTable
from utils.utils import *


def show_all_books():
    """
     Prints a list of all books stored in database
    """
    print(constants.VIEW_ALL_BOOKS)
    print(constants.LINE)
    x = PrettyTable()
    x.field_names = constants.HEADERS_NO_DESC
    all_values = LIBRARY.get_all_values()
    all_values_no_headers = all_values[1:]
    for i in all_values_no_headers:
        x.add_rows(
            [i[:-1]]
        )

    print(x)
    print(constants.LINE)


def show_book_details():
    show_all_books()
    select = int(input("Which book details would you like to see?: "))
    clear_terminal()
    book_id = select + 1
    znaleziona = LIBRARY.row_values(book_id)
    book_to_display = znaleziona[:-1]
    book_description = str(znaleziona[-1])
    x = PrettyTable()
    x.field_names = constants.HEADERS_NO_DESC
    x.add_rows([book_to_display])
    print(constants.SHOW_BOOK_DETAILS)
    print(x)
    print(f"\n{constants.DESCRIPTION}: ")
    wrap_text(book_description)


def edit_book():
    print(constants.EDIT_BOOK)
    show_all_books()
    select = int(input("Which book would you like to edit?: "))
    clear_terminal()
    book_id = select + 1
    znaleziona = LIBRARY.row_values(book_id)
    description = znaleziona[-1]
    book_description = str(description)
    book_no_desc = znaleziona[:-1]

    x = PrettyTable()
    x.field_names = constants.HEADERS_NO_DESC
    x.add_rows([book_no_desc])
    print(x)

    print(f"\n{constants.DESCRIPTION}: ")
    wrap_text(book_description)

    while True:
        print("""
        1. Title 
        2. Author
        3. Category
        4. Status
        5. Description
        6. Return to main menu
        """)
        user_choice = input("Please select what do you want to edit: ")
        edit_cell = ""
        if user_choice == "1":
            edit_cell = (input("Please enter new title: "))
            book_no_desc[1] = edit_cell
            LIBRARY.update_cell(book_id, 2, edit_cell)
            clear_terminal()
            print(f'Book title updated successfully to "{edit_cell.title()}".\n')
            print("Keep editing this book or return to main menu.")
        elif user_choice == "2":
            edit_cell = (input("Please enter new author: "))
            book_no_desc[2] = edit_cell
            LIBRARY.update_cell(book_id, 3, edit_cell)
            clear_terminal()
            print(f'Book author updated successfully to "{edit_cell.title()}".\n')
            print("Keep editing this book or return to main menu.")
        elif user_choice == "3":
            edit_cell = (input("Please enter new category: "))
            book_no_desc[3] = edit_cell
            LIBRARY.update_cell(book_id, 4, edit_cell)
            clear_terminal()
            print(f'Book category updated successfully to "{edit_cell.upper()}".\n')
            print("Keep editing this book or return to main menu.")
        elif user_choice == "4":
            updated_desc = (input("Please select 1) if book is READ and 2) if NOT READ: "))
            if updated_desc == "1":
                edit_cell = "Read"
            elif updated_desc == "2":
                edit_cell = "Not read"
            book_no_desc[4] = edit_cell
            LIBRARY.update_cell(book_id, 5, edit_cell)
            clear_terminal()
            print(f'Book status updated successfully to "{edit_cell.lower()}."\n')
            print("Keep editing this book or return to main menu.")
        elif user_choice == "5":
            edit_cell = (input("Please enter new description: "))
            LIBRARY.update_cell(book_id, 6, edit_cell)
            clear_terminal()
            print(f"Book description updated successfully.\n")
            print("Keep editing this book or return to main menu.")
        elif user_choice == "6":
            break


def add_book():
    print(constants.ADD_BOOK)
    book_to_be_added = []

    title = input("Please enter the title: ")
    author = input("Please enter the author: ")
    category = input("Please enter book category: ")
    status = input('Please select "1" if book is READ and "2" if NOT READ: ')
    read_status = ""

    if status == "1":
        read_status = "Read"
    elif status == "2":
        read_status = "Not read"

    description = input("Please enter book description: ")
    print(book_to_be_added)
    book_to_be_added.extend([title, author, category, read_status, description])
    print(book_to_be_added)
    clear_terminal()
    print(constants.LINE)
    first_empty_row = len(LIBRARY.get_all_values())

    book_to_be_added.insert(0, first_empty_row)  # adds ID as a first item in book list
    for header, item in zip(range(len(constants.HEADERS_NO_DESC)), range(len(book_to_be_added))):
        print(f"{constants.HEADERS_NO_DESC[header]}: {book_to_be_added[item]}")

    print(f"\n{constants.DESCRIPTION}: ")
    wrap_text(book_to_be_added[-1])

    print(constants.LINE)
    are_you_sure = input(" \nConfirm adding this book. Y/N: ")

    if are_you_sure == "y":
        LIBRARY.append_row(book_to_be_added)
        print("Adding book to database...")
        print("Book added successfully.")
    else:
        clear_terminal()
        menu.show_menu()


def remove_book():
    print(constants.REMOVE_BOOK)
    show_all_books()
    delete_book = int(input("Please select a book to remove [#ID]: "))
    row_to_delete = delete_book + 1
    new_row_to_delete = str(row_to_delete)
    delete_this_book = LIBRARY.acell("B" + new_row_to_delete).value
    author_of_deleted_book = LIBRARY.acell("C" + new_row_to_delete).value
    book_status = LIBRARY.acell("E" + new_row_to_delete).value
    print(f"\nThe book: {delete_this_book} by {author_of_deleted_book} will be removed. The book is {book_status}.\n")

    are_you_sure = input("Are you sure you want to delete this book? y/n: ")
    if are_you_sure == "y":
        LIBRARY.delete_rows(row_to_delete)
        print("Removing book...")
        renumber_column_id()
    # else - chose what to do, return to previous screen?


def quit_app():
    """
     This function prints goodbye message to the user
    """
    print("Thank you for using the app, bye!")
    print("Terminating...")


