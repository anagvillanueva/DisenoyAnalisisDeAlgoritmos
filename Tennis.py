# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 08:51:15 2021
PROGRAMA: Tennis 
@author: Ana Fernanda Gutierrez Villanueva
"""


print("PARTIDO DE TENNIS")

""" Ambos comienzan en lo love, es decir cero """

jugador1 = "love"
jugador2 = "love"

4
print("RONDA 1 - ¿Cual es el puntaje del jugador 1?")
puntaje1 = input()
jugador1 = puntaje1
print("El jugador 1 tiene:",puntaje1)

print("RONDA 1 - ¿Cual es el puntaje del jugador 2?")
puntaje2 = input()
jugador2 = puntaje2
print("El jugador 2 tiene:",puntaje2)

print("")
print("RESULTADO:")

"""Condicionales"""
if (jugador1 == jugador2):
    print ("Deuce - Empate")
elif (jugador1 > jugador2):
    print("El jugador 1 ha ganado, WIN")
elif (jugador2 < jugador1):
    print ("El jugador 2 ha ganado, WIN")

