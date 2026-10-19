#!/usr/bin/env python3
def pow(a, b):
    if b < 0:
        return 1 / pow(a, -b)
    total = 1
    for i in range(b):
        total = total * a
    return total
print(pow(2, -2))
