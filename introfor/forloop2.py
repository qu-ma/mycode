#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   nesting an if-statement inside of a for loop"""

# create a list of strings
vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
# create a second list of strings
approved_vendors = ["cisco", "juniper", "big_ip"]
# loop across the list called vendors

for i in vendors:
    print(f"The vendor is: {i}")

    if i not in approved_vendors:
        print(f"{i} is not an approved vendor.")

print("For loop finished")
