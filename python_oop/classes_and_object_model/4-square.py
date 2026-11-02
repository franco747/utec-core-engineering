#!/usr/bin/env python3
"""Módulo que define la clase Square"""


class Square:
    """Representa un cuadrado"""

    def __init__(self, size=0):
        """Inicializa el cuadrado con un tamaño igual a 0 o mayor"""
        self.size = size

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

    def area(self):
        """Devuelve el área del cuadrado"""
        return self.__size ** 2