#!/usr/bin/python3

with open("dnsservers.txt", "r") as dnsfile:
    for svr in dnsfile:
        svr = svr.strip('\n')

        if svr.endswith('org'):
            with open("org-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")

        elif svr.endswith('com'):
            with open("com-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")

