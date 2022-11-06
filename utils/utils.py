from api.google_sheets_api import LIBRARY
import os
import textwrap


def clear_terminal():
    """
    Clears terminal for better screen readability
    """

    os.system("cls" if os.name == "nt" else "clear")
    print("terminal cleared!")
    print('\n' * 20)  # prints 20 line breaks


def wrap_text(text):
    wrapper = textwrap.TextWrapper(width=79)
    wrapped_text = wrapper.fill(text=text)
    print(wrapped_text)


def renumber_column_id():
    """
    Renames values in column A in the worksheet to keep ID values in order when book is removed
    """
    col = LIBRARY.col_values(1)
    new_col = col[1:]
    id_val = 1
    row_val = 2

    for i in new_col:
        LIBRARY.update_acell("A" + str(row_val), id_val)  # renumbering ID value to keep order
        id_val += 1
        row_val += 1

    print("Database successfully updated.")

# dlugosc = len(LIBRARY.get_all_values()) + 1
# print(dlugosc) # nastepny pusty wiersz


def sort_books():
    """
    Sorts column one ascending
    """
    LIBRARY.sort((1, 'asc'))  # ascending by column 1
