#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - strings test true"""

ipchk = input("Apply an IP address: ")

# a string tests as True
if ipchk == "192.168.70.1":
   print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
elif ipchk:
   print("Looks like the IP address was set: " + ipchk)
else:
   print("You did not provide input.")
