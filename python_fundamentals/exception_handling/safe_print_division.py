#!/usr/bin/env python3
def safe_print_division(a, b):
    resultado = None
    try:
        resultado = a / b
        return a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(resultado))
        if __name__ == "__main__":
            (safe_print_division(10, 2))
