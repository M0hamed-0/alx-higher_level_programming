#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary):
        values = a_dictionary.values()
        max_value = max(values)
        new_dict = list(filter(lambda item: (item[1] == max_value),
                        a_dictionary.items()))
        return (new_dict[0][0])
    else:
        return (None)
