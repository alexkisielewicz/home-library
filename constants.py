"""
Constants
"""
from api.google_sheets_api import *

LINE = "###############################################################################"
HEADERS = LIBRARY.row_values(1)
HEADERS_NO_DESC = HEADERS[:-1]
HEADERS_NO_DESC_NO_ID = HEADERS[:-1]
DESCRIPTION = LIBRARY.row_values(1).pop()
ALL_VALUES = LIBRARY.get_all_values()
ALL_VALUES_NO_HEADER = ALL_VALUES[1:]
APP = "Home Library"

ADD_BOOK = """Here you can add new book to your library. \n
You will be asked to enter book title, author, category and short description.
Choose if you have read the book or not. Book ID will be generated automatically. 
"""
EDIT_BOOK = "Here you can edit all book details and update it in the database."
REMOVE_BOOK = "Here you can remove selected book from the database."
VIEW_ALL_BOOKS = "This is the list of all your books."
SHOW_BOOK_DETAILS = "This is detailed view of the book."
