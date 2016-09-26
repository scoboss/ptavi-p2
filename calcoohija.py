#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Continuamos programando la calculadora añadiendo ahora la multiplicacion y la division, excluido entre 0.

import sys

#definimos numero como antes para que acepte tanto int como float

def numero(operando):
    return float(operando)

class Calculadora():

    def plus(self, num1, num2):
        return num1 + num2
    def minus(self, num1, num2):
        return num1 - num2

class CalculadoraHija(Calculadora):

    def producto(self, num1, num2):
        return num1 * num2
    def division(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")

def resultado(num1, operacion, num2):
    result = CalculadoraHija()
    if (operacion == "suma"):
        solucion = result.plus(num1, num2)
    elif (operacion == "resta"):
        solucion = result.minus(num1, num2)
    elif (operacion == "multiplica"):
        solucion = result.producto(num1, num2)
    elif (operacion == "divide"):

        solucion = result.division(num1, num2)
    else:
        sys.exit("Error solo suma, resta, multiplica, divide")
    return solucion

if __name__ == "__main__":
    try:
        numero1 = sys.argv[1]
        operacion = sys.argv[2]
        numero2 = sys.argv[3]
    except IndexError:
        sys.exit("Error los parametros son 3; numero operador numero")
    try:
        num1 = numero(numero1)
        num2 = numero(numero2)
    except ValueError:
        sys.exit("Error:Non numerical parameters")
    print (resultado(num1, operacion, num2))





