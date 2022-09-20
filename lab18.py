#!/usr/bin/python3
""" Lab 18 challenge """

import random

def main():
    wordbank = ["indentation", "spaces"] 

    tlgstudents = ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    random.shuffle(tlgstudents)

    wordbank.append(4)

    num = input("Enter a number between 0 and 18: ")

    if num.isdigit():
        student_name = tlgstudents[int(num)]
    else:
        student_name = num

    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")    

if __name__ == "__main__":
    main()
