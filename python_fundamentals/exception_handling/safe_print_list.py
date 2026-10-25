#!/usr/bin/env python3
def safe_print_list(my_list=[], x=0):
    cont = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            cont = cont + 1
        except IndexError:
            break
    print()
    return cont


if __name__ == "__main__":
    print(safe_print_list([1, 2, 3, 4, 5], 7))
