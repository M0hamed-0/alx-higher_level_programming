#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import os

    args = sys.argv
    argsCount = len(args)
    fileName = os.path.basename(__file__)
    file_path = f"./{fileName}"
    i = 0

    if argsCount == 1:
        print("0 arguments.")
    elif argsCount == 2:
        print("1 argument:")
        print("1: {}".format(args[1]))
    else:
        print("{:d} arguments:".format(argsCount - 1))
        while i < argsCount - 1:
            if args == file_path:
                continue
            i += 1
            print("{:d}: {:s}".format(i, args[i]))
