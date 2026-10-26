#!/usr/bin/env python3
"""Este modulo crea o reescribe un archivo.

Devuelve la cantidad de caracteres escritos.
"""


def write_file(filename="", text=""):
    """Escribe text en filename y devuelve los caracteres escritos."""
    with open(filename, "w", encoding="UTF-8") as file_1:
        write = file_1.write(text)
    return write


if __name__ == "__main__":
    write_file("file_1.txt", "hola como va tu dia")
    