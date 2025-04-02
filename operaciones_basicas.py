"""
Este script corrige errores de estilo según las normas PEP 8.
"""

class OperacionesBasicas:
    """
    Clase para realizar operaciones matemáticas básicas, como la suma y la resta.
    """

    def __init__(self):
        """Inicializa el resultado a cero."""
        self.resultado = 0

    def sumar(self, a, b):
        """Suma dos números y guarda el resultado."""
        self.resultado = a + b

    def restar(self, a, b):
        """Resta dos números y guarda el resultado."""
        self.resultado = a - b

    def obtener_resultado(self):
        """Devuelve el resultado actual."""
        return self.resultado


class CalculadoraPromedio:  # pylint: disable=too-few-public-methods
    """
    Clase para calcular el promedio de una lista de valores.
    """

    def __init__(self, valores):
        """Inicializa la lista de valores."""
        self.valores = valores

    def calcular_promedio(self):
        """Calcula y devuelve el promedio de la lista de valores."""
        return sum(self.valores) / len(self.valores)


# Variables globales
NUMEROS = [1, 2, 3, 4, 5]
NUM1 = 10
NUM2 = 20

# Ejecución principal
if __name__ == "__main__":
    # Uso de la clase OperacionesBasicas
    operaciones = OperacionesBasicas()
    operaciones.sumar(NUM1, NUM2)
    print(f"El resultado de la suma es: {operaciones.obtener_resultado()}")

    operaciones.restar(NUM1, NUM2)
    print(f"El resultado de la resta es: {operaciones.obtener_resultado()}")

    # Uso de la clase CalculadoraPromedio
    calculadora_promedio = CalculadoraPromedio(NUMEROS)
    promedio = calculadora_promedio.calcular_promedio()
    print(f"El promedio de los números es: {promedio}")
