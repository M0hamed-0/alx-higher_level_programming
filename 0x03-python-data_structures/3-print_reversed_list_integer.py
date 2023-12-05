#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 0
    listlen = len(my_list)
    my_list.reverse()
    while i < listlen:
        print("{:d}".format(my_list[i]))
        i += 1
