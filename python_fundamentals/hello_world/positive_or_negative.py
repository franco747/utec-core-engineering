#!/usr/bin/env python3
number = __import__('random').randint(-10, 10)
if (number > 0):
    print(number,"es positivo")
elif(number < 0):
    print(number,"es negativo")
else:
    print(number,"es cero")
