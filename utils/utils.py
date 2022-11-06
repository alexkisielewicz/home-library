from api.google_sheets_api import LIBRARY
import os
import textwrap
import constants
from prettytable import PrettyTable


def clear_terminal():
    """
    Clears terminal for better screen readability
    """
    os.system("cls" if os.name == "nt" else "clear")
    print("terminal cleared!")
    print('\n' * 20)  # prints 20 line breaks


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

    print("Database successfully updated.")


def check_prefix():
    """
    Checks if title starts with "The" and converts it to format "Title, The"
    :return: title
    """
    text = input("Please enter the title: ")
    title_lower = text.lower()

    if title_lower.startswith("the "):
        prefix = ", The"
        rewrite_title = title_lower[4:]
        new_title = rewrite_title + prefix
        title = new_title.title()
        print("Converted to: ", title)
    else:
        title = title_lower.title()

    return title


def sort_books(col, order):
    """
    Sorts database records
    """
    LIBRARY.sort((col, order))  # ascending by title
    # LIBRARY.sort((2, "asc"))  # ascending by author


def print_all_database():
    x = PrettyTable()
    x.field_names = constants.HEADERS_NO_DESC
    x.align["ID"] = "r"
    x.align["Title"] = "l"
    x.align["Author"] = "l"
    x.align["Category"] = "l"
    x.align["Status"] = "l"
    all_values_no_headers = constants.ALL_VALUES[1:]
    for i in all_values_no_headers:
        x.add_rows(
            [i[:-1]]
        )
    print(x)
