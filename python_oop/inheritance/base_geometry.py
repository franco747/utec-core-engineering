#!/usr/bin/env python3
"""Módulo que define la clase BaseGeometry"""


class BaseGeometry:
    """Clase base para figuras geométricas"""

    def area(self):
        """Calcula el área, aún no implementado en la clase base"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que value sea un entero mayor que 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
