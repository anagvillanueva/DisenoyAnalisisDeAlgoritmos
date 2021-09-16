# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:58:47 2021

@author: Gutierrez Villanueva Ana Fernanda 
"""
def combinacion(combinar, lista):
	new_comb=[]
	for x in combinar:
		pto=lista.index(x[len(x)-1])
		for j in range(pto,len(lista)):	
			if lista[j] not in x and lista[len(lista)-1] not in x:	
				new_comb.append(x+lista[j]) 
	print (new_comb)
	return new_comb 
 
 
 
lista=["1","2","3"]
print ("C O M B I N A C I O N E S")
combinacion(lista, lista)