import numpy as np
import csv
from Contrato import contrato
class MC():
    __dimension=0
    __cantidad=0
    __incremento=1
    def __init__(self,dimension,incremento=1):
        self.__dimension=dimension
        self.__cantidad=0
        self.__contrato=np.empty(dimension,dtype=contrato)
    def leer(self):
        archivo=open("Equipos.csv","r")
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for Fila in reader:
            if band==False:
                band=True
            else:
                if(self.__cantidad==self.__dimension):
                    self.__dimension+=self.__incremento
                    self.__contrato.resize(self.__dimension)
                uncontrato=contrato(Fila[0],Fila[1],Fila[2])
                self.__contrato[self.__cantidad]=uncontrato
                self.__cantidad+=1
        archivo.close()
