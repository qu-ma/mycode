#!/usr/bin/python3

import uuid

howmany = int(input("How many UUIDS should be generated? "))

print("Generating UUIDs...")

for rando in range(howmany):
    print(uuid.uuid4())
