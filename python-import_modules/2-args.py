#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    print("{} argument{}.".format(len(args), "" if len(args) == 1 else "s"))
    for i, args in enumerate(args, start=1):
        print("{}: {}".format(i, args))
