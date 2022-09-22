#!/usr/bin/python3

import os

grep = "grep -i 'vampire' dracula.txt"

os.system(grep)

vampire_counter = os.system(f"{grep} | wc -l")
print(vampire_counter)

os.system(f"{grep} >> vamp.txt")

#vampire_counter = 0
#
#with open("dracula.txt","r") as dracula:
#    for line in dracula:
#        if "vampire" in line.lower():
#            print(line)
#            vampire_counter += 1
#
#            with open("vampytimes.txt", "a") as vampy:
#                vampy.write(line)
#
#print(vampire_counter)
