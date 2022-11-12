"""
Constants used throughout the app
"""
from api.google_sheets_api import *
from colorama import Fore

# app constants

HEADERS = LIBRARY.row_values(1)
HEADERS_NO_DESC = HEADERS[:-1]
HEADERS_NO_DESC_NO_ID = HEADERS[:-1]
DESCRIPTION = LIBRARY.row_values(1).pop()
ALL_VALUES = LIBRARY.get_all_values()
ALL_VALUES_NO_HEADER = ALL_VALUES[1:]
APP = "Home Library"
LINE = "###############################################################################"  # 79 characters long

# descriptions of the functionalities
ADD_BOOK = """
Now you can add a new book to your library. \n
You will be asked to enter book title, author, category and short description.
Choose if you have read the book or not. Book ID is generated automatically. 
"""

EDIT_BOOK = "Here you can update all book details.\n"

REMOVE_BOOK = "Here you can remove selected book from the database.\n"

VIEW_ALL_BOOKS = f"This is the list of all your books."

SHOW_BOOK_DETAILS = "This is detailed view of the book entry."

END_SCREEN = """
It was developed by Aleksander Kisielewicz 
for Diploma in Full Stack Software Development 
at Code Institute.

Visit my profiles: 
https://github.com/alexkisielewicz
https://www.linkedin.com/in/alekkisielewicz/
"""
