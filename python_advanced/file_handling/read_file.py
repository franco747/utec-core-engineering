#!/usr/bin/env python3
#!/usr/bin/env python3
"""Este módulo lee un archivo de texto e imprime su contenido."""
def read_file(filename=""):
    """Lee el archivo filename e imprime su contenido."""
    with open(filename, "r", encoding="UTF-8") as my_file_0:
        leer = my_file_0.read()
        print(leer, end="")


if __name__ == "__main__":
    read_file("my_file_0.txt")
    
