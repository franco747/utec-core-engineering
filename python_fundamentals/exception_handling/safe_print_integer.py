#!/usr/bin/env python3
def safe_print_integer(value):
        
    try:
        print("{}".format(value))
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    print(safe_print_integer(89))
