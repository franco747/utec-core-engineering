#!/usr/bin/env python3
"""Modulo que define la clase Rectangle"""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectangulo"""

    def __init__(self, width, height):
        """Inicializa el rectangulo validando ancho y alto"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
