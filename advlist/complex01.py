#!/usr/bin/python3

"""Alta3 Research | RZFeeser
   List - simple list"""


def main():
    # Create list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # Display list1
    print(list1)

    # Display list1[1]
    print(list1[1])

    # Create list2
    list2 = ["juniper"]
    
    # Extend list1 by list2
    list1.extend(list2)

    # Display list1
    print(list1)
    
    # Create list3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]
    
    # Append list1 by list3
    list1.append(list3)

    # Display complex list1
    print(list1)

    # Display list of IP Addresses
    print(list1[4])

    # Display first item in list
    print(list1[4][0])


if __name__ == "__main__":
    main()
