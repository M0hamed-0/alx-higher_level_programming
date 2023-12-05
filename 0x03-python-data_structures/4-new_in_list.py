#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    mylist = my_list.copy()
    if idx < 0:
        return (mylist)
    elif idx > (len(mylist) - 1):
        return (mylist)
    else:
        mylist[idx] = element
        return (mylist)
