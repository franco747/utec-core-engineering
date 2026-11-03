#!/usr/bin/env python3
"""Módulo que define la clase Square"""


class Square:
    """Representa un cuadrado"""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa el cuadrado con tamaño y posición"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Devuelve el tamaño del cuadrado"""
        return self.__size

    @size.setter
    def size(self, value):
        """Asigna el tamaño validando tipo y valor"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Devuelve la posición del cuadrado"""
        return self.__position

    @position.setter
    def position(self, value):
        """Asigna la posición validando que sea tupla de 2 enteros >= 0"""
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Devuelve el área del cuadrado"""
        return self.__size ** 2

    def my_print(self):
        """Imprime el cuadrado con el carácter #"""
        print(self)

    def __str__(self):
        """Devuelve el cuadrado como cadena, respetando la posición"""
        if self.__size == 0:
            return ""
        fila = " " * self.__position[0] + "#" * self.__size
        return "\n" * self.__position[1] + "\n".join([fila] * self.__size)
