import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('home-library')

LIBRARY = SHEET.worksheet('library')


def welcome():
    from header import logo, show_menu
    logo()
    show_menu()

print(LIBRARY.acell("A1").value)

# welcome()


# TODO
# * User Interact with the terminal
# * Validate User input
# * Exception handling
# * Terminal colours
# * Clearing of the screen
# * Split code into multiple .py files
# * google_sheets_api.py
# * write type hinting

# api (--> this is a python library)
#     __init__.py
#     google_sheets_api.py
#     finnhub_api.py
# utils
#     __init__.py
#     printing_utils.py
# constants.py
# run.py
#     from api.google_sheets_api import XYZ  # example
