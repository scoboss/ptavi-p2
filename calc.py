#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

#modificamos en clase para miultiplicar y dividir pero para la practica la entregaremos como al inicio.


def plus(op1, op2):
    """ Function to sum the operands """
    return op1 + op2


def minus(op1, op2):
    """ Function to substract the operands """
    return op1 - op2


if __name__ == "__main__":


    try:
        operando1 = float(sys.argv[1])
        operando2 = float(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = minus(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
