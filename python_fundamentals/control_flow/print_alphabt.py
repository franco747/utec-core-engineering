#!/usr/bin/env python3
result = ""
for i in range(97, 123):
    if (chr(i) != "e" and chr(i) != "q"):
        result += chr(i)
print("{}".format(result))
