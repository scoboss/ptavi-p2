#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

#definimos numero para que los operandos se efectuen en float, 
#aunque sean sumas y restas si efectuamos las operacion en int 
#si introducimos un float nos da error. Mientras que si usamos 
#float podemos introducirlo en int y sigue funcionando.

def definonumero(operando):
    return float(operando)


#la clase calculadora va tener los metodos suma y resta, 
#que en objetos definimos como funciones. 
#Como seguimos del ejercicio anterior (calc.py) continuamos con el nombre 
#de plus y minus.

class Calculadora():
    def plus(self, num1, num2):
        return num1 + num2
    def minus(self, num1, num2):
        return num1 - num2

#como nos pide el ejercicio tenemos que tener un programa principal el cual 
#tome los parametros e instancie objeto de la clase Calculadora.

def resultado(num1, operacion, num2):
    result = Calculadora()
    if (operacion == "suma"):
        solucion = result.plus(num1, num2)
    elif (operacion == "resta"):
        solucion = result.minus(num1, num2)
    else:
        sys.exit("Solo puede sumar y restar")
    return solucion

if __name__ == "__main__":
    try:
        numero1 = sys.argv[1]
        operacion = sys.argv[2]
        numero2 = sys.argv[3]
    except IndexError:
        sys.exit("Error los parametros son 3; operador numero operador")
    try:
        num1 = definonumero(numero1)
        num2 = definonumero(numero2)
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    print (resultado(num1, operacion, num2))


