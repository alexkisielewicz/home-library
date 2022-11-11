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
    print(f"Books are now sorted {default_sorting_method}.")
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

    length = len(LIBRARY.get_all_values()[1:])  # finds last entry ID

    while True:
        user_choice = int(input("Which book details would you like to see?: "))

        if user_choice in list(range(1, length + 1)):
            wierszdb = user_choice + 1  # because of list's zero notation
            print("wierszdb: ", wierszdb)
            lokacja = LIBRARY.row_values(wierszdb)
            print(lokacja)
            print(len(lokacja))
            if len(lokacja) == 0:
                clear_terminal()
                print(f"There's no book with ID #{lokacja}. Please select a book from  list.\n")
                show_book_details()
                break
            else:
                pass
            print("lokacja: ", lokacja)
            book_to_display = lokacja[:-1]  # find last row in the database
            print("book_to_display: ", book_to_display)
            book_description = str(lokacja[-1])  # extract selected book's description from all values
            print("book_description: ", book_description)

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
            print("Please choose book from the list, from 1 to 12.\n")
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
            print("Skoro mamy ustawione sortowanie: ", default_sorting_method, " to musimy zmienic")
            print("Zmieniamy na przeciwny ", optional_sorting_method)
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

    length = len(LIBRARY.get_all_values())
    print(length)

    while True:
        print(constants.EDIT_BOOK)
        show_all_books()
        user_choice = int(input("Which book would you like to edit?: "))
        clear_terminal()
        book_row = user_choice + 1
        print("Book_id to: ", book_row)
        book_entry = LIBRARY.row_values(book_row)
        print("Book row to: ", book_row)
        print("Book_entry: ", book_entry)
        if len(book_entry) == 0:  # checks if book with selected ID exists.
            clear_terminal()
            print(f"There's no book with ID #{user_choice}. Please select book from the list.\n")
            edit_book()
            break
        else:
            pass
        book_description = book_entry[-1]
        print("book_description: ", book_description)

        print("description to: ", book_description)
        book_description_str = str(book_description)
        book_no_desc = book_entry[:-1]
        print("Book_no_desc to: ", book_no_desc)

        def print_edited_book():
            print(constants.EDIT_BOOK)
            print(constants.LINE)
            x = PrettyTable()
            x.field_names = constants.HEADERS_NO_DESC  # assigns table's headers from first row in DB
            x.align["Title"] = "l"  # align column to the left
            x.add_rows([book_no_desc])
            print(x)  # prints created table
            print(f"\n{constants.DESCRIPTION}: ")
            wrap_text(book_description_str)
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
            # validate_num_range(user_choice, 1, 6)
            validate_input_range(user_choice, 1, 6)
            edit_cell = ""
            if user_choice == "1":
                edit_cell = check_prefix()
                book_no_desc[1] = edit_cell.title()
                LIBRARY.update_cell(book_row, 2, edit_cell.title())
                print("Updating database...")
                clear_terminal()
                print(f'Book title updated successfully to "{edit_cell.title()}".\n')
                print("Keep editing this book or return to main menu.")

            elif user_choice == "2":
                edit_cell = (input("Please enter new author: "))
                book_no_desc[2] = edit_cell.title()
                LIBRARY.update_cell(book_row, 3, edit_cell)
                clear_terminal()
                print(f'Book author updated successfully to "{edit_cell.title()}".\n')
                print("Keep editing this book or return to main menu.")
            elif user_choice == "3":
                edit_cell = (input("Please enter new category: "))
                book_no_desc[3] = edit_cell.capitalize()
                LIBRARY.update_cell(book_row, 4, edit_cell)
                clear_terminal()
                print(f'Book category updated successfully to "{edit_cell.capitalize()}".\n')
                print("Keep editing this book or return to main menu.")
            elif user_choice == "4":
                updated_desc = (input('Please select "1" if book is READ and "2" if NOT READ: '))
                validate_input_range(updated_desc, 1, 2)
                if updated_desc == "1":
                    edit_cell = "Read"
                elif updated_desc == "2":
                    edit_cell = "Not read"
                book_no_desc[4] = edit_cell
                LIBRARY.update_cell(book_row, 5, edit_cell)
                clear_terminal()
                print(f'Book status updated successfully to "{edit_cell.lower()}."\n')
                print("Keep editing this book or return to main menu.")
            elif user_choice == "5":
                edit_cell = (input("Please enter new description: ")).capitalize()
                validate_string(user_choice)
                LIBRARY.update_cell(book_row, 6, edit_cell)
                book_description_str = edit_cell
                clear_terminal()
                print(f"Book description updated successfully.\n")
                print("Keep editing this book or return.")

            elif user_choice == "6":
                show_all_books()  # returns to previous menu
                break

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
    validate_num_range(status, 1, 2)
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
                LIBRARY.append_row(book_to_be_added)
                print("Adding book to the database... Please wait...")

                if optional_method == default_sorting_method:  # sorting is required to keep order in database
                    sort(default_method)
                else:
                    sort(optional_method)
                print("Book added successfully.")
                break

            elif "n" in are_you_sure or "N" in are_you_sure:
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

    while True:
        length = len(LIBRARY.get_all_values()[1:])
        length1 = len(LIBRARY.get_all_values())
        print("Długość to: ", length)
        print("length1 to: ", length1)
        delete_book = input("Please select a book to remove (#ID):) ")
        validate_input_range(delete_book, 1, length)

        # range cannot be interpreted as integer!

        row_to_delete = int(delete_book) + 1
        find_row = str(row_to_delete)
        delete_this_book = LIBRARY.acell("B" + find_row).value
        author_of_deleted_book = LIBRARY.acell("C" + find_row).value
        book_status = LIBRARY.acell("E" + find_row).value
        clear_terminal()
        confirm = f'The book "{delete_this_book.title()}" by {author_of_deleted_book.title()} will be removed. ' \
                  f'The book is {book_status.lower()}.'
        wrap_text(confirm)

        while True:
            are_you_sure = input("\nAre you sure you want to delete this book? Y/N: ")
            if validate_yes_no(are_you_sure):

                if "y" in are_you_sure or "Y" in are_you_sure:
                    LIBRARY.delete_rows(row_to_delete)
                    print("Removing book, please wait...")
                    renumber_id_column()  # to keep numeration in order after entry deletion.
                    clear_terminal()
                    print("Book removed. Database updated successfully.")
                    break
                elif "n" in are_you_sure or "N" in are_you_sure:
                    print("Aborting... Database hasn't been changed.")
                    break
            else:
                print("Incorrect input, aborting...")
                menu.show_menu()

        break


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
