#!/usr/bin/python3

with open("vlanconfig.cfg", "r") as configfile:
    configlist = configfile.readlines()

print(configlist)
