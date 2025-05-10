#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv[1:]
    count = len(arg)
    if count == 0:
        print("0")
    total = 0
    for i in arg:
        total += int(i)
    print(total)        
