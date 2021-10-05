
def cajero(monto):
    billetes = (500,200,100) #O(3) O(3)
    monedas = (20,10,5,1,0.5) #O(5) O(5)
    
    i = 0 #O(4) O(1)
    resultado = "" #O(0) O(1)
    validar = False #O(1) O(1)
    
    for billete in billetes: #O(1) O(na)
      while validar is False: #O(0) O(na)
        aux = monto 
        monto = monto - billete 
        if monto >= 0: #O(0) O(na)
          i = i+1 
        else:
          monto = aux 
          validar = True #O(0) O(3)
      if i > 0: #O(0) O(na)
        resultado = resultado + "\n" + f"{i} Billetes de: ${billete}" #O(17) O(3)
      validar = False 
      i = 0 
    
    for moneda in monedas: #O(1) O(na)
      while validar is False: #O(0) O(na)
        aux = monto
        monto = monto - moneda #O(0) O(5*n)
        if monto >= 0: #O(0) O(na)
          i =  i+1 #O(0) O(5*n)
        else:
          monto = aux 
          validar = True 
      if i > 0: #O(0) O(na)
        resultado = resultado + "\n" + f"{i} Monedas de: ${moneda}" #O(17) O(5)
      validar = False #O(0) O(5)
      i = 0 
      
    return resultado
    
print("¿Cual es el monto? $459")
print(cajero(459))