#!/usr/bin/env python3
def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as my_file_0:
        leer = my_file_0.read()
        print(leer, end="")


if __name__ == "__main__":
    read_file("my_file_0.txt")
    