# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 21:14:11 2021

@author: Ana Fernanda Gutierrez Villanueva 
"""

print("Celula viva = 1 | Celula muerta = 0")

fila = int(input("Numero de filas:"))

columna = int(input("Numero de columnas:"))


class matriz:
    viva = 1
    muerta = 0
    def __init__(self, fila, columna, valor):
        self.__fila = fila
        self.__columna = columna
        self.__array = [[valor for x in range(self.__columna+2)] for y in range(self.__fila+2)]


    def numerofil(self):
        return self.__fila

    def numerocol(self):
        return self.__columna

    def getItem(self, fila, columna):
        return self.__array[fila][columna]

    def setItem(self, fila, columna, valor):
        self.__array[fila][columna] = valor

    def limpiar(self, valor = 0):
        for filas in range(self.__fila):
            for columnas in range(self.__columna):
                self.__array[filas][columnas] = valor

    def tablero(self):
        for r in range(1,self.numn()+1):
            for c in range(1,self.numcol()+1):
                if self.getItem(r,c) == 0:
                    print(" 0 ", end="")
                else:
                    print(" 1 ", end="")
            print("")
            
            
    def gen_uno(self, poblacion):
        self.limpiar()
        for celula in poblacion:
            self.setItem(celula[0], celula[1], self.viva)

def ejecucion(self, generaciones):
       count = 1
       while count <= generaciones:
           for r in range(1,self.numeroren()+1):
               for c in range(1,self.numcol()+1):
                   vecinos = self.getItem(r,c+1) + self.getItem(r,c-1) + self.getItem(r-1,c) \
                           + self.getItem(r+1,c) + self.getItem(r-1,c-1) + self.getItem(r+1,c-1) \
                           + self.getItem(r-1,c+1) + self.getItem(r+1,c+1)
                   if self.getItem(r,c) == 1 and vecinos == 2:
                       self.setItem(r, c, self.viva)

                   elif self.getItem(r,c) == 1 and vecinos == 3:
                       self.setItem(r, c, self.viva)

                   elif self.getItem(r,c) == 1 and vecinos == 0:
                       self.setItem(r, c, self.muerta)

                   elif self.getItem(r,c) == 1 and vecinos == 1:
                       self.setItem(r, c, self.muerta)

                   elif self.getItem(r,c) == 1 and vecinos >= 4:
                       self.setItem(r, c, self.muerta)

                   elif self.getItem(r,c) == 0 and vecinos == 3:
                       self.setItem(r, c, self.viva)

                   elif self.getItem(r,c) == 0 and vecinos < 3:
                       self.setItem(r, c, self.muerta)


           self.tablero()
           print("\n")
           count = count + 1
       print("ya acabo las "+ str(generaciones))


tab = matriz(6,5,0)
tab.tablero()
print("-----------------------")
tab.generacion1([(3,2),(3,3),(3,4),(4,2),(4,4),(5,2),(5,3),(5,4)])
tab.tablero()
print("\n")
tab.ejecucion(10)