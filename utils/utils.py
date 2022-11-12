from api.google_sheets_api import LIBRARY, CONFIG
import os
import textwrap
import app_menu as menu
import constants
import random
from prettytable import PrettyTable
from scripts import functions
from colorama import Fore

default_method = CONFIG.acell('B1').value  # either "by title" or "by author"
optional_method = CONFIG.acell('B2').value  # is always opposite value to default_method

first_book_id = ""
last_book_id = ""


def database_check():
    while True:
        is_empty = len(LIBRARY.row_values(2))  # checks if there is a record below DB headers
        if is_empty == 0:
            clear_terminal()
            print("Database is empty, add at least one book to continue.")
            menu.show_menu()
            break
        else:
            break


def how_many_books():
    all_books = LIBRARY.col_values(1)[1:]  # list of IDs of all books
    global first_book_id
    global last_book_id

    if len(all_books) == 1:
        return True
    elif len(all_books) > 1:
        first_book_id = all_books[0]
        last_book_id = all_books[-1]
        return False

    return first_book_id, last_book_id


def validate_num_range(user_input, first_val, last_val):  # e. g main menu with options 1-7
    """
    Checks if user input is withing the range of possible options.
    Any input out of desired range will show user a message containing a range of options.
    :param user_input: this is user input
    :param first_val: this is first option from the range of options
    :param last_val:  this is the last option from the range of options
    :returns True if user's input is valid
    :returns False if user's input is invalid
    """
    options = list(range(first_val, last_val + 1))
    allowed_options = [str(i) for i in options]

    if user_input in allowed_options:
        return True
    else:
        clear_terminal()
        print(f"Wrong input, please select option from {first_val} to {last_val} to continue...\n")
        return False


def validate_input_range(user_input, first_val, end):
    print("Zakres to: ", first_val, end)
    end += 1  # plus one because of list's zero notation
    if user_input.isnumeric():
        print("is numeric?: ", user_input.isnumeric())
        print("is in the range?: ", user_input in range(first_val, end))
        print(list(range(first_val, end)))
        print(type(int(user_input)))
        if int(user_input) in range(first_val, end):
            print(list(range(first_val, end)))
            print(len(list(range(first_val, end))))
            print("Correct input!")
            pass
        else:
            print("This is not allowed.")
    else:
        print("This is not a number, it must be a string")


def validate_string(user_input):
    if user_input.isalnum():
        print("OK, it's a string")
        return True
    else:
        print("Not alpha-numerical")
        return False


def validate_input(user_input, min_value, max_value):
    try:
        try:
            user_input = int(user_input)
        except TypeError:
            print("Invalid input.")
            return False
        if user_input in range(min_value, max_value + 1):
            return True
        raise ValueError()
    except ValueError:
        print("Invalid input.")
        return False


def validate_yes_no(user_input):
    valid_options = ["y", "Y", "n", "N"]
    if user_input in valid_options:
        return True
    else:
        return False


def clear_terminal():
    """
    Clears terminal for better screen readability
    """
    os.system("cls" if os.name == "nt" else "clear")
    print("terminal cleared!")
    print('\n' * 20)  # prints 20 line breaks to simulate CLS in PyCHarm IDE


def wrap_text(text):
    """
    Wraps long strings over 79 characters to the new line.
    Used to correctly display books descriptions.
    :param text:
    """
    wrapper = textwrap.TextWrapper(width=79)
    wrapped_text = wrapper.fill(text=text)
    print(wrapped_text)


def renumber_id_column():
    """
    Renames values in column A in the worksheet to keep ID values in order when book is removed
    """
    col = LIBRARY.col_values(1)
    new_col = col[1:]
    id_val = 1
    row_val = 2

    for _ in new_col:
        LIBRARY.update_acell("A" + str(row_val), id_val)  # renumbering ID value to keep order
        id_val += 1
        row_val += 1
    print("Updating database...")


def check_prefix():
    """
    Checks if title starts with "The" and converts it to format "Title, The"
    :return: title
    """
    text = input("Please enter the title: ")
    title_lower = text.lower()

    if title_lower.startswith("the "):
        prefix = ", The"
        rewrite_title = title_lower[4:]  # slice of a string - remove first 4 char "the ".
        new_title = rewrite_title + prefix
        title = new_title.title()
        print("Converted to: ", title)
    else:
        title = title_lower.title()

    return title


def sort_books(col, order):
    """
    Sorts database records alphabetically.
    :param col - number of the column in Google Sheets
    :param order - can be chosen "asc", or "des"
    """
    LIBRARY.sort((col, order))  # sorts values in worksheet LIBRARY


def sort(sorting_order):
    global default_method
    global optional_method
    if sorting_order == default_method:
        print("sorting order is: ", sorting_order, "default_method is: ", default_method, "do nothing")
    elif sorting_order == optional_method:
        if default_method == "by author":
            print("Sorting database by title. Please wait...")
            CONFIG.update_acell("B1", "by title")  # write method to database
            CONFIG.update_acell("B2", "by author")  # write method to database
            functions.default_sorting_method = "by title"  # changing value so can be updated in functions.py
            functions.optional_sorting_method = "by author"  # changing value so can be updated in functions.py
            default_method = "by title"
            optional_method = "by author"
            sort_books(2, "asc")
            renumber_id_column()
        elif default_method == "by title":
            print("Sorting database by author. Please wait...")
            CONFIG.update_acell("B1", "by author")  # writing method to database
            CONFIG.update_acell("B2", "by title")  # writing method to database
            functions.default_sorting_method = "by author"  # changing value so can be updated in functions.py
            functions.optional_sorting_method = "by title"  # changing value so can be updated in functions.py
            default_method = "by author"
            optional_method = "by title"
            sort_books(3, "asc")
            renumber_id_column()


def print_all_database():
    """
    Gets all values from the database and prints to the terminal
    all records in table easy to read.
    """
    x = PrettyTable()
    x.field_names = constants.HEADERS_NO_DESC
    x.align["ID"] = "r"  # aligns column to the right
    x.align["Title"] = "l"  # aligns column to the left
    x.align["Author"] = "l"
    x.align["Category"] = "l"
    x.align["Status"] = "l"
    all_values = LIBRARY.get_all_values()  # gets all values from DB
    all_values_no_headers = all_values[1:]  # all values without the first row
    for i in all_values_no_headers:
        x.add_rows(
            [i[:-1]]  # each iteration adds a row to the table, we skip the header
        )
    print(x)


def random_not_read():
    all_books = LIBRARY.get_all_values()[1:]  # without headers
    not_read = []

    for book in all_books:
        if "Not read" in book[4]:
            not_read.append(book)

    if len(not_read) > 0:
        random_book = random.choice(not_read)
        suffix = ", The"
        prefix = "The "
        title = random_book[1]

        if suffix in title:
            short = title[:-5]  # a title without last 5 characters
            new_title = prefix + short
            title = new_title

        print("Looking for your next read?")
        print(f"Why don't you grab \"{title}\" by {random_book[2]}. It's still not read.")
