#!/usr/bin/python3
""" Lab 24 - Challenge 01 """
import shutil
import os

def main():

    # Start script in this specific directory
    os.chdir("/home/student/mycode")
    
    # Copy a file
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # The following line will create the directory if it does not exist already
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
