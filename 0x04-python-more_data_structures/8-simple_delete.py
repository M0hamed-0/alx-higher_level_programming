#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_list = list(a_dictionary)
    for k in new_list:
        if k == key:
            del(a_dictionary[k])
    return (a_dictionary)
