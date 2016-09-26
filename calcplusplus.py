#!/usr/bin/python3 
# -*- coding: utf-8 -*- 

import sys
import csv
from calcplus import resultados_fichero

if __name__ == "__main__":
    fichero = sys.argv[1]
    with open(fichero) as ficheroejercicio:
        resultados_fichero(ficheroejercicio)

