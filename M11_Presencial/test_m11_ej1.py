# test_rectangulo_oop.py
# Archivo de pruebas para la clase Rectangulo.

import pytest

try:
    from m11_rectangulo_ej1 import Rectangulo
except ImportError:
    pytest.fail(
        "No se pudo importar la clase 'Rectangulo' del archivo 'student_code_m12_ex1.py'.")


def test_inicializacion_atributos():
    """Verifica que los atributos se inicializan correctamente."""
    r = Rectangulo(10, 20)
    assert r.ancho == 10
    assert r.alto == 20


def test_calcular_area_enteros():
    """Prueba el método calcular_area con números enteros."""
    r = Rectangulo(8, 5)
    assert r.calcular_area() == 40


def test_calcular_area_flotantes():
    """Prueba el método calcular_area con números de punto flotante."""
    r = Rectangulo(2.5, 4)
    assert r.calcular_area() == 10.0


def test_cuadrado():
    """Prueba el caso de un cuadrado (ancho y alto iguales)."""
    cuadrado = Rectangulo(7, 7)
    assert cuadrado.calcular_area() == 49


def test_objeto_diferente():
    """Verifica que otro objeto tenga sus propios datos y resultados."""
    r1 = Rectangulo(10, 2)
    r2 = Rectangulo(5, 5)
    assert r1.calcular_area() == 20
    assert r2.calcular_area() == 25


# make this module executable
if __name__ == "__main__":
    # If the tests pass, print a success message
    if pytest.main([__file__]) == 0:
        print("✅ Pruebas pasadas para el ejercicio de clases y objetos.")
    # If the tests fail, print an error message
    else:
        print("❌ Error en el código")
        print("Este módulo no se puede ejecutar directamente. Usa pytest para correr las pruebas.")
# This module is not meant to be run directly. Use pytest to run the tests.
