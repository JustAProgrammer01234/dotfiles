#!/usr/bin/python3 

# This script is used to create links to each dotfile here to the home directory.  

from pathlib import Path

import os 

for dotfile in os.listdir():
    if not dotfile.startswith(".") or dotfile == ".git": 
        continue

    print(f"Creating link for: {dotfile}")

    cwd = os.getcwd()
    home = Path.home()

    try:
        os.link(f"{cwd}/{dotfile}", f"{home}/{dotfile}")
    except Exception as e:
        print(f"An error occured while creating link for {dotfile} :(") 
        print(f"Error message: {e}")
    else:
        print(f"Successfully created link for {dotfile}")

    print() 


print("Done executing!")