# -*- coding: utf-8 -*-
"""
Ana Fernanda Gutierrez Villanueva

Ejercicio 1 

"""

def numero(telefono):
    import re
    telefono = telefono.replace(' ', '')
    if (telefono[0:3] == "+52"):
       return telefono
    else:
        num = '+52'
        telefono= num + telefono
        return telefono
    
   
print(numero("55 10825614"))

print(numero("+52 7555 123456"))
