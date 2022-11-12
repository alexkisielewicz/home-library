import utils.utils
from utils.utils import *


default_sorting_method = CONFIG.acell("B1").value  # either "by title" or "by author"
print("default method is set to: ", default_sorting_method)  # will be removed
optional_sorting_method = CONFIG.acell("B2").value  # always opposite value to default_sorting_method
print("optional method is set to: ", optional_sorting_method)  # will be removed


def show_all_books():
    """
     Prints to terminal a list of all books stored in the database.
    """
    database_check()
    print(constants.VIEW_ALL_BOOKS)
    print(constants.LINE)
    print_all_database()
    print(constants.LINE)


def show_book_details():
    """
    Prints to the terminal a single book entry selected by the user.
    Takes user input and looks up the database for selected book,
    extracts and assigns all the information to variables and print
    detailed info as a table.
    """
    database_check()
    show_all_books()  # shows user all the books
    allowed_input = LIBRARY.col_values(1)[1:]

    while True:
        user_choice = input("Which book details would you like to see?: ")

        if user_choice in allowed_input:
            db_row = int(user_choice) + 1  # because of list's zero notation
            book_id = LIBRARY.row_values(db_row)
            book_to_display = book_id[:-1]  # find last row in the database
            book_description = str(book_id[-1])  # extract selected book's description from all values

            x = PrettyTable()
            x.field_names = constants.HEADERS_NO_DESC
            x.add_rows([book_to_display])
            clear_terminal()
            print(constants.SHOW_BOOK_DETAILS)
            print(constants.LINE)
            print(x)
            print(f"\n{constants.DESCRIPTION}: ")
            wrap_text(book_description)
            print(constants.LINE)
        else:
            clear_terminal()
            how_many_books()
            print(f"No such record! Please select #ID from 1 to {utils.utils.last_book_id}.\n")
            show_book_details()

        break


def change_sorting_method():
    """
    Changes sorting method
    """
    database_check()
    show_all_books()
    while True:
        print(f"Books are displayed in alphabetical order and sorted {default_sorting_method}.")
        print("How would you like to sort them?")
        if default_sorting_method == "by title":
            print(f"""
                    1. {optional_sorting_method.capitalize()}
                    2. Return
                    """)
        elif default_sorting_method == "by author":
            print(f"""
                    1. {optional_sorting_method.capitalize()}
                    2. Return
                    """)
        user_choice = input("Select 1 or 2: ")
        clear_terminal()
        validate_num_range(user_choice, 1, 2)
        if user_choice == "1":
            sort(optional_sorting_method)
            show_all_books()
            break
        elif user_choice == "2":
            show_all_books()
            break


def edit_book():
    """
    Allows user to edit all database values for each book such as:
    title, author, category, read status and description.
    """
    database_check()
    allowed_input = LIBRARY.col_values(1)[1:]

    while True:
        print(constants.EDIT_BOOK)
        show_all_books()
        user_choice = input("Which book would you like to edit?: ")
        clear_terminal()

        if user_choice in allowed_input:

            db_row = int(user_choice) + 1
            book_id = LIBRARY.row_values(db_row)
            book_description = str(book_id[-1])
            book_no_desc = book_id[:-1]

            def print_edited_book():
                print(constants.EDIT_BOOK)
                print(constants.LINE)
                x = PrettyTable()
                x.field_names = constants.HEADERS_NO_DESC  # assigns table's headers from first row in DB
                x.align["Title"] = "l"  # align column to the left
                x.add_rows([book_no_desc])
                print(x)  # prints created table
                print(f"\n{constants.DESCRIPTION}: ")
                wrap_text(book_description)
                print(constants.LINE)

            while True:
                print_edited_book()
                print("""
                1. Title 
                2. Author
                3. Category
                4. Status
                5. Description
                6. Return
                """)
                user_choice = input("What do you want to edit? Select 1-6: ")
                validate_num_range(user_choice, 1, 6)
                # validate_input_range(user_choice, 1, 6)
                edit_cell = ""

                if user_choice == "1":
                    edit_cell = check_prefix()
                    # validate CHECK_PREFIX !
                    book_no_desc[1] = edit_cell.title()
                    LIBRARY.update_cell(db_row, 2, edit_cell.title())
                    print("Updating database...")
                    clear_terminal()
                    print(f'Book title updated successfully to "{edit_cell.title()}".\n')
                    print("Keep editing this book or return to main menu.")

                elif user_choice == "2":
                    edit_cell = (input("Please enter new author: "))
                    book_no_desc[2] = edit_cell.title()
                    LIBRARY.update_cell(db_row, 3, edit_cell)
                    clear_terminal()
                    print(f'Book author updated successfully to "{edit_cell.title()}".\n')
                    print("Keep editing this book or return to main menu.")

                elif user_choice == "3":
                    edit_cell = (input("Please enter new category: "))
                    # VALIDATE HERE
                    book_no_desc[3] = edit_cell.capitalize()
                    LIBRARY.update_cell(db_row, 4, edit_cell)
                    clear_terminal()
                    print(f'Book category updated successfully to "{edit_cell.capitalize()}".\n')
                    print("Keep editing this book or return to main menu.")

                elif user_choice == "4":
                    while True:
                        updated_desc = (input('Please select "1" if book is READ and "2" if NOT READ: '))
                        if validate_num_range(updated_desc, 1, 2):
                            if updated_desc == "1":
                                edit_cell = "Read"
                                book_no_desc[4] = edit_cell
                                LIBRARY.update_cell(db_row, 5, edit_cell)
                                clear_terminal()
                                print(f'Book status updated successfully to "{edit_cell.lower()}".\n')
                                print("Keep editing this book or return to main menu.")
                                break
                            elif updated_desc == "2":
                                edit_cell = "Not read"
                                book_no_desc[4] = edit_cell
                                LIBRARY.update_cell(db_row, 5, edit_cell)
                                clear_terminal()
                                print(f'Book status updated successfully to "{edit_cell.lower()}".\n')
                                print("Keep editing this book or return to main menu.")
                                break
                        else:
                            clear_terminal()
                            print(f"Wrong input, please try again...\n")

                elif user_choice == "5":
                    edit_cell = (input("Please enter new description: ")).capitalize()
                    validate_string(user_choice)
                    LIBRARY.update_cell(db_row, 6, edit_cell)
                    book_description = edit_cell
                    clear_terminal()
                    print(f"Book description updated successfully.\n")
                    print("Keep editing this book or return.")

                elif user_choice == "6":
                    show_all_books()  # returns to previous menu
                    break

        else:
            clear_terminal()
            how_many_books()
            print(f"No such record! Please select #ID from 1 to {utils.utils.last_book_id}.\n")
            edit_book()

        break


def add_book():
    """
    Allows user to add new book to database using user input with following values:
    author, title, category, read status and description.
    The ID of the book is generated and added automatically for each new entry.
    Function looks up the database for first empty row and inserts new entry there.
    """
    print(constants.ADD_BOOK)
    print(constants.LINE)

    book_to_be_added = []

    title = check_prefix()  # checks if book title starts with "The" and returns "Title, The"

    author = input("Please enter the author: ").title()
    validate_string(author)
    category = input("Please enter book category: ").capitalize()
    validate_string(category)
    status = input('Please select "1" if book is READ and "2" if NOT READ: ')
    validate_num_range(status, 1, 2)  # only input 1 or 2 is allowed
    read_status = ""

    if status == "1":
        read_status = "Read"
    elif status == "2":
        read_status = "Not read"

    description = input("Please enter book description: ").capitalize()
    validate_string(description)
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

    while True:
        are_you_sure = input(" \nConfirm adding this book. Y/N: ")
        if validate_yes_no(are_you_sure):

            if "y" in are_you_sure or "Y" in are_you_sure:
                clear_terminal()
                LIBRARY.append_row(book_to_be_added)
                print("Adding book to the database...")

                if optional_method == default_sorting_method:  # sorting is required to keep order in database
                    sort(default_method)
                else:
                    sort(optional_method)
                print("Book added successfully.")
                break

            elif "n" in are_you_sure or "N" in are_you_sure:
                clear_terminal()
                print("Aborting...")
                break
        else:
            print("Incorrect input, aborting...")
            menu.show_menu()


def remove_book():
    """
    Function allows user to remove database entry for selected book.
    Entry deletion is followed by renumbering book's ID values to keep numeration in order without the gaps.
    """
    database_check()

    print(constants.REMOVE_BOOK)
    show_all_books()
    allowed_input = LIBRARY.col_values(1)[1:]
    how_many_books()

    while True:
        user_choice = input("Please select a book to remove (#ID): ")

        if user_choice in allowed_input:

            db_row = int(user_choice) + 1
            row_str = str(db_row)
            # book_id = LIBRARY.row_values(db_row)
            delete_title = LIBRARY.acell("B" + row_str).value
            delete_author = LIBRARY.acell("C" + row_str).value
            delete_status = LIBRARY.acell("E" + row_str).value
            clear_terminal()
            confirm = f'The book "{delete_title.title()}" by {delete_author.title()} will be removed. ' \
                      f'The book is {delete_status.lower()}.'
            wrap_text(confirm)

            while True:
                are_you_sure = input("\nAre you sure you want to delete this book? Y/N: ")
                if validate_yes_no(are_you_sure):

                    if "y" in are_you_sure or "Y" in are_you_sure:
                        LIBRARY.delete_rows(db_row)
                        clear_terminal()
                        print("Removing book, please wait...")
                        renumber_id_column()  # to keep numeration in order after entry deletion.
                        print("Book removed. Database updated successfully.")
                        menu.show_menu()
                        break
                    elif "n" in are_you_sure or "N" in are_you_sure:
                        clear_terminal()
                        print("Aborting... Database hasn't been changed.")
                        menu.show_menu()
                        break
                else:
                    clear_terminal()
                    print("Wrong input, please select \"Y\" or \"N\"...")


        else:
            clear_terminal()
            how_many_books()
            print(f"No such record! Please select #ID from 1 to {utils.utils.last_book_id}.\n")
            remove_book()


def quit_app():
    """
     This function prints goodbye message to the user
    """
    while True:
        print("Why not add another book...?:)")
        are_you_sure = input("\nAre you sure you want to quit? Y/N: ")
        validate_yes_no(are_you_sure)

        if "y" in are_you_sure or "Y" in are_you_sure:
            clear_terminal()
            print(f"Thank you for using {constants.APP} app!")
            print(constants.END_SCREEN)
            random_not_read()
            print("\nTerminating...")
            break
        else:
            menu.show_menu()
            break
