#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv

from calcoohija import CalculadoraHija
from calcoohija import definonumero
from calcoohija import resultado


#importamos solo calculadorahija puesto que haciendo eso incluimos calculadora


def resultados_operaciones(lineas):
    for operandos in lineas:
        operando = operandos.split(',')
        operacion = operando[0]
        numero = definonumero(operando[1])
        for i in operando[2:]:
            number = int(i)
            num1 = definonumero(number)
            num2 = definonumero(number)
            solucion = resultado(num1, operacion, num2)
            numero = definonumero(solucion)
    return solucion


def lineas_fichero(lineas):
    for line in lineas:
        lineas = line.split()
        solucion = resultados_operaciones(lineas)
        print (solucion)


def resultados_fichero(ficheroejercicio):
    lineas = ficheroejercicio.readlines()
    lineas_fichero(lineas)


if __name__ == "__main__":
    fichero = sys.argv[1]
    ficheroejercicio = open(fichero, 'r')
    resultados_fichero(ficheroejercicio)
    ficheroejercicio.close()
