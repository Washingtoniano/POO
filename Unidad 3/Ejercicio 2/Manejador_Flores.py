import numpy as np
from Flores import flores
import csv
class ManejadorF():
    __dimension=0
    __incremento=1
    __cantidad=0
    def __init__(self,dimension=0,incremento=1):
        self.__dimension=dimension
        self.__incremento=incremento
        self.__flores=np.empty(dimension,dtype=flores)
    def leer (self):
        archivo=open("flores.csv",'r')
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                if self.__cantidad==self.__dimension:
                    self.__dimension+=self.__incremento
                    self.__flores.resize(self.__dimension)
                unaflor=flores(fila[0],fila[1],fila[2],fila[3])
                self.__flores[self.__cantidad]=unaflor
                self.__cantidad+=1
    def dimension(self):
            return self.__flores
    def id (self):
        return self.__flores.id()
