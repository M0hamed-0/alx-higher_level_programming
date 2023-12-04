#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import os

    args = sys.argv
    argsCount = len(args)
    fileName = os.path.basename(__file__)
    file_path = f"./{fileName}"
    i = 0
    summ = 0

    if argsCount == 1:
        print("0")
    elif argsCount == 2:
        summ = args[0] = args[1]
        print("{}".format(summ))
    else:
        while i < argsCount - 1:
            if args == file_path:
                continue
            i += 1
            summ += int(args[i])
        print("{}".format(summ))
