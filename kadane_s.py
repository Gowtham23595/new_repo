#!/usr/bin/env python 3

#find the largest sub array

def print_list(list):
    print(list)
    return

def main():
    #get the list
    list_1 = input("Please enter the iput in commas")
    list_2 = list_1.split(",")
    print("The values in the list  " + str(print_list(list_2)) + "\n")
    kadanae(list_2)
    return


if __name__ == "main":
    main()