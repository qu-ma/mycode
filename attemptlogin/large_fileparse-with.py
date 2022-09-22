#!/usr/bin/python3

import re

pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

loginfail = 0

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:
    for line in kfile:
        if "- - - - -] Authorization failed" in line:
            print(pattern.search(line))
            loginfail += 1

print("The number of failed log in attempts is", loginfail)
