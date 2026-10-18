#!/usr/bin/env python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            resultado = chr(ord(i) - 32)
        else:
            resultado = (i)
        print(resultado, end="")
    print()
