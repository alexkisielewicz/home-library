# print welcome message with logo
def logo():
    print("""
    ██   ██  ██████  ███    ███ ███████     ██      ██ ██████  ██████   █████  ██████  ██    ██ 
    ██   ██ ██    ██ ████  ████ ██          ██      ██ ██   ██ ██   ██ ██   ██ ██   ██  ██  ██  
    ███████ ██    ██ ██ ████ ██ █████       ██      ██ ██████  ██████  ███████ ██████    ████   
    ██   ██ ██    ██ ██  ██  ██ ██          ██      ██ ██   ██ ██   ██ ██   ██ ██   ██    ██    
    ██   ██  ██████  ██      ██ ███████     ███████ ██ ██████  ██   ██ ██   ██ ██   ██    ██                                                                           
    """)
    print("Welcome to Home Library app, you can manage all your books here. Please select option 1-5 to continue.")


def menu():
    print("""
            1. Add book
            2. Edit book
            3. Remove book
            4. View all books
            5. Quit
            """)
    print("Please select option from 1-5: ")


def show_menu():
    while True:
        menu()
        user_choice = input()
        try:
            int(user_choice)
        except:
            print("That's not a number. Please select number from 1 to 5.")
            show_menu()
        if user_choice == "1":
            print("Add book")
            break
        elif user_choice == "2":
            print("Edit book")
        elif user_choice == "3":
            print("Remove book")
        elif user_choice == "4":
            print("View all books")
        elif user_choice == "5":
            print("Thank you for using the app, bye!")
            break
        elif int(user_choice) > 5:
            print("Number out of range. Please select number from 1 to 5.")


logo()
show_menu()
