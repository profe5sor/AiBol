try:
    import pyfiglet
    import subprocess
    import os
    import re
    import sys
    from colorama import * 
    import platform
except ImportError:
    os.system("pip3 install pyfiglet", shell=True)


os.system("cls")

ascii_banner = pyfiglet.figlet_format("Aibol")
print(ascii_banner)
init()
print(Fore.CYAN + " [+] ©profe5sor 2024")
print(Fore.CYAN + " [+] AiBol is a text-to-speech program created by Pankaj Prajapati")
print(Fore.RED + "-----------------------------------------------------")
print(Fore.WHITE + "App Version : 1.1.2")
print(Fore.WHITE + "Detected OS: " + platform.system())
print(Fore.WHITE + "OS Release: " + platform.release())
print(Fore.RED + "-----------------------------------------------------")
print(Fore.CYAN + "Developer : Pankaj Prajapati aka Profe5sor")

input('\n [=] Press Enter to get Developer Contact')
print("Please wait")
print("Developer : Pankaj Prajapati")
print("Email : prfsr04@gmail.com")
print("Github : github.com/profe5sor")

#print(Style.RESET_ALL)


