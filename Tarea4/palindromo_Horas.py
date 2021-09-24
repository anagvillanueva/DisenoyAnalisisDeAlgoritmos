# -*- coding: utf-8 -*-
"""
AFGV 

"""

def paliHoras():
  hora = ""
  contador = 0
  for x in range(0,24):
    for k in range(0,60):
      if x < 10 and k < 10:
        hora = f"0{x}:0{k}"
      elif x < 10:
        hora = f"0{x}:{k}"
      elif k < 10:
        hora = f"{x}:0{k}"
      else:
        hora = f"{x}:{k}"
      if hora[0:2] == hora[4]+hora[3]:
        print(hora)
        contador += 1
  print(f"Total: {contador}")
  