#!/usr/bin/python3

configfile = open("vlanconfig.cfg", "r")

print(configfile.read())
configfile.close()

configfile = open("vlanconfig.cfg", "r")

configlist = configfile.readlines()
print(configlist)

for i in configlist:
    print(i.strip())
   #print(i, end="")

configfile.close()
