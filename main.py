import os
from colorama import Fore
import requests
import time
import pyperclip
import json
import sys

config = json.load(open("config.json", "r"))
clear = lambda: os.system('cls')


clear()

lib = config["libpath"]
boollib = bool(lib)
if boollib == False:
    print(f"{Fore.RED}[!] - You did not enter a path for the lib. Check it in config.json{Fore.RESET}")
    sys.exit()

while True:
    clear()
    menu = input(f"""
Hex Patch Helper Made By {Fore.LIGHTGREEN_EX}YeetDisDude#0001
Version 0.1
{Fore.LIGHTCYAN_EX}[1]{Fore.RESET} - Get hex from function
{Fore.LIGHTCYAN_EX}[2]{Fore.RESET} - Make GameGuardian Script
{Fore.LIGHTCYAN_EX}[3]{Fore.RESET} - Arm to Hex Converter
{Fore.LIGHTCYAN_EX}[4]{Fore.RESET} - Hex to arm Converter\n""")

    if menu == "1":
        clear()
        offset = eval(input(f"{Fore.LIGHTCYAN_EX}Enter your offset with 0x:{Fore.RESET}\n"))
        bytes = int(input(f"{Fore.LIGHTCYAN_EX}How many bytes do you want to get?{Fore.RESET}\n"))
        with open(lib, 'rb') as f:
            f.seek(0x3F89CE4)
            hexfromoffset = f.read(bytes).hex().upper()
        print(f"{Fore.LIGHTRED_EX}{bytes}{Fore.RESET} Bytes from the offset {Fore.LIGHTRED_EX}0x{offset}{Fore.RESET}:\n{hexfromoffset}")
        pyperclip.copy(hexfromoffset)
        print("Copied to clipboard")
        time.sleep(5)

    if menu == "2":
        clear()
        n = 23 #8 bytes is 23 characters so this will be used to replace the first 23 characters with patchedhex
        hextosearch = input("Enter the hex you want to search:\n")
        checkhextosearch = bool(hextosearch)
        if checkhextosearch == False:
            print(f"{Fore.RED}[!] - You can't leave this empty.{Fore.RESET}")
            sys.exit()
        hexforpatch = input("Enter the hex you want to patch it to (8 bytes):\n")
        checkhexforpatch = bool(hexforpatch)
        if checkhexforpatch == False:
            print(f"{Fore.RED}[1] - You can't leave this empty{Fore.RESET}")
            sys.exit()
        patchedhex = hexforpatch + hextosearch[n:]
        with open('custom_script.lua') as f:
            script = f.read()
        print("Script:\n",script)
        pyperclip.copy(script)
        print("Copied to clipboard")
        with open('generated_scripts/Script.lua', 'w') as f:
            f.write(script)
        print(f"Saved to {Fore.LIGHTRED_EX}Generated Scripts{Fore.RESET} Folder")
        time.sleep(5)

    if menu == "3":
        clear()
        asm = input("Assembly:\n")
        payload = {
            "asm": asm
        }
        r = requests.post("https://armconverter.com/api/convert", json=payload)
        r = r.json()
        arm = r["hex"]["arm"][1]
        arm64 = r["hex"]["arm64"][1]
        clear()
        print(f"{Fore.LIGHTRED_EX}Asm: {asm}\n{Fore.LIGHTRED_EX}Arm64: {Fore.RESET}{arm64}\n{Fore.LIGHTRED_EX}Arm: {Fore.RESET}{arm}\n")
        tocopy = input(f"{Fore.LIGHTRED_EX}Which do you want to copy?\n[1] - Arm64\n[2] - Arm\n[3] - Both\n[4] - Exit\n")
        if tocopy == "1": #arm64
            pyperclip.copy(arm64)
            print(f"\nCopied to clipboard:\n{Fore.LIGHTRED_EX}{arm64}{Fore.RESET}")
            time.sleep(1)
        if tocopy == "2": #arm
            pyperclip.copy(arm)
            print(f"\nCopied to clipboard:\n{Fore.LIGHTRED_EX}{arm}{Fore.RESET}")
            time.sleep(1)
        elif tocopy == "3": #all
            tocopyall = f"Arm64: {arm64}\nArm: {arm}"
            pyperclip.copy(tocopyall)
            print("\nCopied to clipboard | Arm64 and Arm")
            time.sleep(1)
            
    if menu == "4":
        clear()
        hexarmconvert = input("hex:\n")
        payload = {
            "hex": hexarmconvert
        }
        r = requests.post("https://armconverter.com/api/convert", json=payload)
        r = r.json()
        arm = r["asm"]["arm"][1]
        arm64 = r["asm"]["arm64"][1]
        clear()
        print(f"{Fore.LIGHTRED_EX}Hex: {hexarmconvert}\n{Fore.LIGHTRED_EX}Arm64: {Fore.RESET}{arm64}\n{Fore.LIGHTRED_EX}Arm: {Fore.RESET}{arm}\n")
        tocopy = input(f"{Fore.LIGHTRED_EX}Which do you want to copy?\n[1] - Arm64\n[2] - Arm\n[3] - Both\n[4] - Exit\n")
        if tocopy == "1": #arm64
            pyperclip.copy(arm64)
            print(f"\nCopied to clipboard:\n{Fore.LIGHTRED_EX}{arm64}{Fore.RESET}")
            time.sleep(1)
        if tocopy == "2": #arm
            pyperclip.copy(arm)
            print(f"\nCopied to clipboard:\n{Fore.LIGHTRED_EX}{arm}{Fore.RESET}")
            time.sleep(1)
        elif tocopy == "3": #all
            tocopyall = f"Arm64: {arm64}\nArm: {arm}"
            pyperclip.copy(tocopyall)
            print("\nCopied to clipboard | Arm64 and Arm")
            time.sleep(1)