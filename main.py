import colorama
import time
import signal
from os import system
from colorama import Fore, Back, Style
import random

def main():
        
    print(Fore.CYAN + "                           _")
    print("                        _ooOoo_")
    print("                       o8888888o         DDOS ATTACKING")
    print("                       88\" . \"88")       
    print(Fore.RED + "                       (| -_- |)")    
    print(Fore.CYAN +"                       O\  =  /O")
    print(Fore.RED +"                    ____/`---'\____   --Buddha's in the system")      
    print(Fore.CYAN +"                  .'  \\|     |//  `.")
    print("                 /  \\|||  :  |||//  \\")
    print("                /  _||||| -:- |||||_  \\")
    print("                |   | \\\  -  /'| |   |")
    print(Fore.RED +"                | \_|  `\`---'//  |_/ |")
    print(Fore.CYAN +"                \  .-\__ `-. -'__/-.  /")
    print("              ___`. .'  /--.--\  `. .'___")
    print("           .\"\" '<  `.___\_<|>_/___.' _> \"" + Fore.RESET)
    print(Fore.CYAN + "          | | :  `- \`. ;`. _/; .'/ /  .' ; |")  
    print("          \  \ `-.   \_\_`. _.'_/_/  -' _.' /")
    print("===========`-.`___`-.__\ \___  /__.-'_.'_.-'================")
    print("                        `=--=-'")

main()


def handler(signum, frame):
    print("\nInterrupción de teclado detectada. Deteniendo el registro...")

signal.signal(signal.SIGINT, handler)

print("1: IP ")
print("2: EXIT ")

while True:
    option = input('==>')
    if option == '1':
        while True:
            option1 = input("PASTE THE VICTIM IP: ")
            octets = option1.split(".")
            valid = True
            for octet in octets:
                if not octet.isdigit() or int(octet) > 255:
                    valid = False
                    break
            if valid:
                break
            print("Error: IP INVALID")

        ip_entered = True

        print("PORT: ")
        port = input('==>')
        print("SOCKS: ")
        socks = input('==>')
        print("Iniciando ataque...")
        time.sleep(5)

        while True:
            try:
                log = print(Fore.RED + "ATACANDO A " + Fore.CYAN + option1, "con "+ Fore.RED  + socks)
                time.sleep(1)
            except KeyboardInterrupt:
                print("\nInterrupción de teclado detectada. Deteniendo el registro...")
                break

    elif option == '2':
        print("Exiting program...")
        break

    else:
        print("Invalid option. Please try again.")

print("Program finished.")