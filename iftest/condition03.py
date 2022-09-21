#!/usr/bin/python3

def main():
    hostname = input("What value should we set for hostname?")

    if hostname.lower() == "mtg":
        print("The hostname was found to be MTG")
        print("hostname matches expected config")

if __name__ == "__main__":
	main()

print("Exiting the script")
