# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 15:11:47 2021

@author: PC
"""
from itertools import chain, combinations

lista = [1, 2, 3]
        

def combinaciones (li):
    return chain(*map(lambda x: combinations(li, x), range(0, len(li)+1)))

for comb in combinaciones(lista):
    print(comb)