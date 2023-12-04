#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    functions_name = dir(hidden_4)
    for name in functions_name:
        if name[0] != '_' and name[1] != '_':
            print(name)
