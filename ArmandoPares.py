# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 09:24:43 2021
Armando Pares
@author: Ana Fernanda Gutierrez Villanueva
"""
print("Lista A:")
listaA=input()
print("Lista B:")
listaB=input()

l1=len(listaA)
l2=len(listaB)

if l1>l2:
    print("Numero de pares:", l2)
    for i in range(l2):
        print("{" ,listaA[i], listaB[i],"}")
        i=i+1
if l2>l1:
    print("Numero de pares:", l1)
    for i in range(l1):
        print("{", listaA[i], listaB[i],"}")
        i=i+1