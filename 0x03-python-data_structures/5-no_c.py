#!/usr/bin/env python3
def no_c(my_string):
    mystring = list(my_string)
    for str in my_string[:]:
        if str == 'c' or str == "C":
            mystring.remove(str)
    mystring = ''.join(mystring)
    return (mystring)
