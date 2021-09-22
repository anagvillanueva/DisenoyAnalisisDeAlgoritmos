# -*- coding: utf-8 -*-

def busqueda_lineal(lista, val_a_buscar):
  contador = 0 #O(1)
  for x in range(len(lista)):
    contador += 1 #O(n)
    if lista[x] == val_a_buscar:
      print(f"Encontrado en la posicion {x}") #O(1)
      break
  return contador
  #O(1 + n+ 1) --> O( 2 + n )

numeros = [2,3,1,23,24,25,10,100,35,8]
comparaciones = busqueda_lineal(numeros, 10)
print(f"{comparaciones} comparaciones")