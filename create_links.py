#!/usr/bin/python3 

# This script is used to create links to each dotfile here to the home directory.  
# Make sure when you are executing the script you are at the directory it's in otherwise it won't work. 

# Things to do:
# 1. Fix the symlink issue. 
# 2. Fix the cli issue. 

from pathlib import Path

import os 
import argparse 

def cmd_parse():
    parser = argparse.ArgumentParser(description="Creates symlink of the dotfiles here to the home directory.") 
    parser.add_argument("-f", "--force",  
        help="Removes the existing dotfiles and replaces them with the dotfiles here.", 
        action="store_true" 
    )
    return parser.parse_args() 
     
def create_links(args):
    cwd = os.getcwd()
    home = Path.home() 

    for dotfile in os.listdir():
        if not dotfile.startswith(".") or dotfile == ".git": 
            continue

        print(f"Creating link for: {dotfile}")

        try:
            dotfile_path = f"{home}/{dotfile}"

            if args.force:
                if os.path.exists(dotfile_path):
                    os.remove(dotfile_path)

            if os.path.isdir(dotfile_path): 
                os.symlink(f"{cwd}/{dotfile}", dotfile_path, target_is_directory=True)
            else:
                os.symlink(f"{cwd}/{dotfile}", dotfile_path)
        except Exception as e:
            print(f"An error occured while creating link for {dotfile} :(") 
            print(f"Error message: {e}")
        else:
            print(f"Successfully created link for {dotfile}")

        print() 


    print("Done executing!")

if __name__ == "__main__":
    args = cmd_parse()
    create_links(args)