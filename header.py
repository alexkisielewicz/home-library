# print welcome message with logo
def logo():
    print("""
    
    ██   ██  ██████  ███    ███ ███████     ██      ██ ██████  ██████   █████  ██████  ██    ██ 
    ██   ██ ██    ██ ████  ████ ██          ██      ██ ██   ██ ██   ██ ██   ██ ██   ██  ██  ██  
    ███████ ██    ██ ██ ████ ██ █████       ██      ██ ██████  ██████  ███████ ██████    ████   
    ██   ██ ██    ██ ██  ██  ██ ██          ██      ██ ██   ██ ██   ██ ██   ██ ██   ██    ██    
    ██   ██  ██████  ██      ██ ███████     ███████ ██ ██████  ██   ██ ██   ██ ██   ██    ██                                                                           
    """)
    print("Welcome to Home Library app")


def show_menu():
    print("""
            1. Add book
            2. Edit book
            3. Remove book
            4. View all books
            5. Quit
            """)
    print("Select option from 1-5: ")

while True:
    show_menu()
    user_choice = int(input())
    if user_choice == 1:
        print("Add book")
    elif user_choice == 2:
        print("Edit book")
    elif user_choice == 3:
        print("Remove book")
    elif user_choice == 4:
        print("View all books")
    elif user_choice == 5:
        print("Thank you for using the app, bye!")
        break
    else:
        print("You must select option from 1 to 5")


