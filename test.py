from colorama import Fore

print(Fore.BLUE + 'Hello')
print(Fore.RED + 'Hello')
print(Fore.YELLOW + 'Hello')
print(Fore.GREEN + 'Hello')

from colorama import Fore, Back, Style
print(Fore.LIGHTMAGENTA_EX + 'light magenta')
print(Fore.CYAN + 'some cyan text')
print("##########################")
print("cos")
print(Fore.RESET)

print(Fore.RED + 'some red text')
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Back.RED + Fore.GREEN + "This is a warning")

print(Style.RESET_ALL)
print("Terefere")

def logo():
    print(Fore.BLUE + """
    ██   ██  ██████  ███    ███ ███████     ██      ██ ██████  ██████   █████  ██████  ██    ██ 
    ██   ██ ██    ██ ████  ████ ██          ██      ██ ██   ██ ██   ██ ██   ██ ██   ██  ██  ██  
    ███████ ██    ██ ██ ████ ██ █████       ██      ██ ██████  ██████  ███████ ██████    ████   
    ██   ██ ██    ██ ██  ██  ██ ██          ██      ██ ██   ██ ██   ██ ██   ██ ██   ██    ██    
    ██   ██  ██████  ██      ██ ███████     ███████ ██ ██████  ██   ██ ██   ██ ██   ██    ██                                                                           
    """)
    print(f"Welcome to Home Library app, you can manage all your books here. Please select option 1-7 to continue.")

logo()
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
