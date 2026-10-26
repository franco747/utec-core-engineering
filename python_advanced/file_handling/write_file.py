#!/usr/bin/env python3
""""Este modulo crea o rescribe el archivo y devuelve cuantos caracteres tiene el archivo adentro"""
def write_file(filename="", text=""):
    """Escribe filename y le escribe texto a filename"""
    with open(filename, "w", encoding="UTF-8") as file_1:
        write = file_1.write(text)
    print(write, end="")


if __name__ == "__main__":
    write_file("file_1.txt","hola como va tu dia")
