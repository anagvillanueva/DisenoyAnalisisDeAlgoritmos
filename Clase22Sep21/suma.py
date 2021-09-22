# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 14:40:29 2021

@author: PC
"""

def suma(num):
    suma = 0
    for i in range(num +1 ):
        suma += i
    print(suma)
    
    import time
 time.time() 
 marca1 = time.time()
 n = 3 
 suma(n)
 marca2 = time.time()
 print( marca2 -marca1)