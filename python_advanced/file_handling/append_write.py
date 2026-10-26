#!/usr/bin/env python3
"""Este modulo anade texto al final de un archivo."""


def append_write(filename="", text=""):
    """Anade text al final de filename y devuelve los caracteres anadidos."""
    with open(filename, "a", encoding="UTF-8") as file_1:
        add = file_1.write(text)
    return add


if __name__ == "__main__":
    print(append_write("file_1.txt", "hola"))
