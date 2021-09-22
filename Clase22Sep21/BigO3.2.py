# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 09:55:56 2021

@author: PC
"""

#Ejercicio 3.2 
numeros = [1,2,3]
numeros2 = [4,5,6]

def unaFuncionCualquiera( lista, lista2 ):
    conteo = 0
    for numero1 in lista:
        for numero2 in lista2:
            print(numero1 , numero2 )
            conteo += 1
    return conteo

    #O(1+2(n*m))
    #((n*m))

conteo = unaFuncionCualquiera(numeros, numeros2)

print( "Final:" , conteo)