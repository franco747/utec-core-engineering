#!/usr/bin/env python3
def islower(c):
   return ord('a') >= ord(c)  and ord('z') <= ord(c)
print(islower('a'))
print(islower('A'))
print(islower('3'))
