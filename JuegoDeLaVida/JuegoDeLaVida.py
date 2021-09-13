# -*- coding: utf-8 -*-
"""
Solamente es una idea de como poder pedir la matriz de cualquier
tamaño y una funcion para revisar si las celulas estan vivas.

@author: Ana Fernanda Gutierrez Villanueva
"""

import numpy as np

n = 1
b = 365

filas = int(input("Numero de filas:"))

columnas = int(input("Numero de columnas:"))

print("")
print("Celula viva = 1 - Celula muerta = 0")
valores = list(map(int, input("Introduce valores separados por un espacio: ").split()))
matriz = np.array(valores).reshape(filas, columnas)

print(matriz)

"""
def checkCelVivas(img,x,y):
    celVivas= 0
    'revisa x+1 cell'
    if img[x+1][y] == n:
        celVivas +=1
    'revisa x-1 cell'
    if img[x-1][y] == n:
        celVivas +=1
    'revisa y+1 cell'
    if img[x][y+1] == n:
        celVivas +=1
    'revisa y-1 cell'
    if img[x][y-1] == n:
        celVivas +=1
    'revisa x+1/y-1 cell'
    if img[x+1][y-1] == n:
        celVivas +=1
    'revisa x+1/y+1 cell'
    if img[x+1][y+1] == n:
        celVivas +=1
    'revisa x-1/y-1 cell'
    if img[x-1][y-1] == n:
        celVivas +=1
    'revisa x-1/y+1 cell'
    if img[x-1][y+1] == n:
        celVivas +=1
    return celVivas
"""