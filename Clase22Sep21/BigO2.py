# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 09:56:41 2021

@author: PC
"""

#Ejercicio 2 
numeros = [1,2,3]

def unaFuncionCualquiera( lista ):
    conteo = 0
    for numero1 in lista:
        for numero2 in lista:
            print(numero1 , numero2 )
            conteo += 1
    return conteo

conteo = unaFuncionCualquiera(numeros)

print( "Final:" , conteo)