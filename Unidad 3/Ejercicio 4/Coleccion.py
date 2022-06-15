import numpy as np
from Calefactor import calefactor
import csv
from Electrico import electrico
from gas import gas
class coleccion():
    __cantidad=0
    __dimension=0
    __incremento=1
    def __init__(self,dimension,incremento=1):
        self.__dimension=dimension
        self.__cantidad=0
        self.__calefactor=np.empty(dimension,dtype=calefactor)
    def leer (self):
        archivo1=open("calefactor-electrico.csv",'r')
        archivo2=open("calefactor-a-gas.csv",'r')
        reader1=csv.reader(archivo1,delimiter=';')
        reader2=csv.reader(archivo2,delimiter=';')
        for fila in reader1:
            if self.__cantidad==self.__dimension:
                self.__dimension=self.__dimension+self.__incremento
                self.__calefactor.resize(self.__dimension)
            unelectrico=electrico(fila[0],fila[1],fila[2])
            self.__calefactor[self.__cantidad]=unelectrico
            self.__cantidad+=1
        for fila in reader2:
            if self.__cantidad==self.__dimension:
                self.__dimension=self.__dimension+self.__incremento
                self.__calefactor.resize(self.__dimension)
            ungas=gas(fila[0],fila[1],fila[2],fila[3])
            self.__calefactor[self.__cantidad]=ungas
            self.__cantidad+=1

    def opcion1(self):
        retor=None
        costo=int(input("Ingresar por teclado el  costo por m3\n"))
        estima=int(input("Ingresar por teclado la cantidad que se estima consumir en m3\n"))
        for elemet in self.__calefactor:
            print(type(elemet))
            if type(elemet)=="gas.gas":
                if elemet.consumo()<estima:
                    print("Marca:{}-Modelo:{}".format(elemet.marca(),elemet.modelo()))
                    retor=elemet
        return retor

    def opcion2(self):
        retor=None
        costo=int(input("Ingresar por teclado el  costo de kilowatt/h \n"))
        estima=int(input("Ingresar por teclado la cantidad que se estima consumir por hora \n"))
        for elemet in self.__calefactor:
            print(type(elemet))
            if type(elemet)=="electrico.electrico":
                if elemet.consumo()<estima:
                    retor=elemet
                    print("Marca:{}-Modelo:{}".format(elemet.marca(),elemet.modelo()))
        return retor
    def opcion3(self,op):
        electrico=None
        gas=None
        if op==1:
            gas=self.opcion1()
        elif op==2:
            electrico=self.opcion2()
        else:
            print(electrico)
            print(gas)


