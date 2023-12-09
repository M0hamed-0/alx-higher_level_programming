#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    if ((type(roman_string) != str) or roman_string is None):
        return (0)
    length = len(roman_string)
    if length == 1:
        return (roman_dic[roman_string])
    sum = 0
    for i in range(0, length - 1):
        if roman_dic[roman_string[i]] < roman_dic[roman_string[i + 1]]:
            sum -= roman_dic[roman_string[i]]
        else:
            sum += roman_dic[roman_string[i]]
    sum += roman_dic[roman_string[length - 1]]
    return (sum)
