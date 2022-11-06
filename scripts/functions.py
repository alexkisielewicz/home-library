import app_menu as menu
from utils.utils import *


def show_all_books():
    """
     Prints to terminal a list of all books stored in the database.
    """
    sort_books(1, "asc")
    print(constants.VIEW_ALL_BOOKS)
    print(constants.LINE)

    print_all_database()

    print(constants.LINE)


def show_book_details():
    """
    Print to the terminal a single book entry from the database.
    """
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


def change_sorting_method():
    """
    Changes sorting method
    """
    show_all_books()
    while True:
        print("Books are displayed in alphabetical order. ")
        print("How would you like to sort them?")
        print("""
        1. By title
        2. By author
        """)
        sorting_order = input("Select 1 or 2: ")

        if sorting_order == "1":
            sort_books(2, "asc")
            print("Updating database, please wait...")
            renumber_id_column()
            clear_terminal()
            show_all_books()
            break
        elif sorting_order == "2":
            sort_books(3, "asc")
            print("Updating database, please wait...")
            renumber_id_column()
            clear_terminal()
            show_all_books()
            break

def edit_book():
    """
    Allows user to edit all database values for each book such as:
    title, author, category, read status and description.
    """
    print(constants.EDIT_BOOK)
    show_all_books()
    select = int(input("Which book would you like to edit?: "))
    clear_terminal()
    book_id = select + 1
    znaleziona = LIBRARY.row_values(book_id)
    description = znaleziona[-1]
    book_description = str(description)
    book_no_desc = znaleziona[:-1]

    def print_edited_book():
        print(constants.EDIT_BOOK)
        x = PrettyTable()
        x.field_names = constants.HEADERS_NO_DESC
        x.align["Title"] = "l"
        x.add_rows([book_no_desc])
        print(x)
        print(f"\n{constants.DESCRIPTION}: ")
        wrap_text(book_description)

    while True:
        print_edited_book()
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
            edit_cell = check_prefix()
            book_no_desc[1] = edit_cell.title()
            LIBRARY.update_cell(book_id, 2, edit_cell.title())
            print("Updating database...")
            clear_terminal()
            print(f'Book title updated successfully to "{edit_cell.title()}".\n')
            print("Keep editing this book or return to main menu.")

        elif user_choice == "2":
            edit_cell = (input("Please enter new author: "))
            book_no_desc[2] = edit_cell.title()
            LIBRARY.update_cell(book_id, 3, edit_cell)
            clear_terminal()
            print(f'Book author updated successfully to "{edit_cell.title()}".\n')
            print("Keep editing this book or return to main menu.")
        elif user_choice == "3":
            edit_cell = (input("Please enter new category: "))
            book_no_desc[3] = edit_cell.capitalize()
            LIBRARY.update_cell(book_id, 4, edit_cell)
            clear_terminal()
            print(f'Book category updated successfully to "{edit_cell.capitalize()}".\n')
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
            edit_cell = (input("Please enter new description: ")).capitalize()
            LIBRARY.update_cell(book_id, 6, edit_cell)
            book_description = edit_cell
            clear_terminal()
            print(f"Book description updated successfully.\n")
            print("Keep editing this book or return to main menu.")

        elif user_choice == "6":
            clear_terminal()
            break


def add_book():
    """
    Allows user to add new book to database using user input with following values:
    author, title, category, read status and description.
    The ID of the book is generated and added automatically for each new entry.
    Function looks up the database for first empty row and inserts new entry there.
    """
    print(constants.ADD_BOOK)
    book_to_be_added = []

    title = check_prefix()  # checks if book title starts with "The" and returns "Title, The"

    author = input("Please enter the author: ").title()
    category = input("Please enter book category: ").capitalize()
    status = input('Please select "1" if book is READ and "2" if NOT READ: ')
    read_status = ""

    if status == "1":
        read_status = "Read"
    elif status == "2":
        read_status = "Not read"

    description = input("Please enter book description: ").capitalize()
    print(book_to_be_added)
    book_to_be_added.extend([title, author, category, read_status, description])
    print(book_to_be_added)
    clear_terminal()
    print(constants.LINE)
    first_empty_row = len(LIBRARY.get_all_values())  # look up database for first empty row

    book_to_be_added.insert(0, first_empty_row)  # adds ID as a first item in book list
    for header, item in zip(range(len(constants.HEADERS_NO_DESC)), range(len(book_to_be_added))):
        print(f"{constants.HEADERS_NO_DESC[header]}: {book_to_be_added[item]}")

    print(f"\n{constants.DESCRIPTION}: ")
    wrap_text(book_to_be_added[-1].capitalize())

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
    """
    Function allows user to remove database entry for selected book.
    Entry deletion is followed by renumbering book's ID values to keep numeration in order without the gaps.
    """
    print(constants.REMOVE_BOOK)
    show_all_books()
    delete_book = int(input("Please select a book to remove [#ID]: "))
    row_to_delete = delete_book + 1
    new_row_to_delete = str(row_to_delete)
    delete_this_book = LIBRARY.acell("B" + new_row_to_delete).value
    author_of_deleted_book = LIBRARY.acell("C" + new_row_to_delete).value
    book_status = LIBRARY.acell("E" + new_row_to_delete).value
    print(f'\nThe book "{delete_this_book.title()}"" by {author_of_deleted_book.title()} will be removed. '
          f'The book is {book_status.lower()}.\n')

    are_you_sure = input("Are you sure you want to delete this book? y/n: ")
    if are_you_sure == "y":
        LIBRARY.delete_rows(row_to_delete)
        print("Removing book, please wait...")
        renumber_id_column()  # renumbers values in ID column to keep numeration in order after entry deletion.
        clear_terminal()
        print("Database updated successfully.")


def quit_app():
    """
     This function prints goodbye message to the user
    """
    print("Thank you for using the app, bye!")
    print("Terminating...")
