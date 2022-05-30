import numpy as np
from Equipo import equipo
import csv
class ME():
    __dimension=0
    __cantidad=0
    __incremento=1
    def __init__(self,dimension,incremento=1):
        self.__dimension=dimension
        self.__cantidad=0
        self.__equipo=np.empty(dimension,dtype=equipo)
    def leer(self):
        #crear archivo de prueba
        archivo=open("Equipos.csv","r")
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for Fila in reader:
            if band==False:
                cant=Fila
                band=True
            else:
                if(self.__cantidad==self.__dimension):
                    self.__dimension+=self.__incremento
                    self.__equipo.resize(self.__dimension)
                unequipo=equipo(Fila[0],Fila[1])
                self.__equipo[self.__cantidad]=unequipo
                self.__cantidad+=1
        archivo.close()
