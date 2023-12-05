#!/usr/bin/python3
def no_c(my_string):
    list1 = list(my_string)
    for str in list1[:]:
        if str == 'c' or str == 'C':
            list1.remove(str)
    new_string = ''.join(list1)
    return (new_string)
