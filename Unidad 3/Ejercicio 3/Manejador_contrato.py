import numpy as np
import csv
from Contrato import contrato
from datetime import datetime

class MC():
    __dimension=0
    __cantidad=0
    __incremento=1
    def __init__(self,dimension,incremento=1):
        self.__dimension=dimension
        self.__cantidad=0
        self.__contrato=np.empty(dimension,dtype=contrato)
    def leer(self,ME,MJ):
        i=0
        j=0
        print("ingrese los datos del contrato:\n")
        inicio=input("Inicio\n")
        fin=input("Fin\n")
        pago=float(input("Pago\n"))
        jugador=input("Jugador\n")
        equipo=input("Equipo\n")
        while i < len(MJ) and str.lower(MJ[i].nombre())!=str.lower(jugador):
            i=i+1
        if i< len(MJ):
            jugador=MJ
        else:
            print("Jugador no encontrado")
        while j<len(ME) and str.lower(ME[j].nombre())!=str.lower(equipo):
            j=j+1
        if i< len(MJ):
            equipo=MJ
        else:
            print("Equipo no encontrado")
        if(self.__cantidad==self.__dimension):
            self.__dimension+=self.__incremento
            self.__contrato.resize(self.__dimension)
        uncontrato=contrato(inicio,fin,pago,jugador,equipo)
        self.__contrato[self.__cantidad]=uncontrato
        self.__cantidad+=1
        MJ[i].contratar(uncontrato)
    def consultar(self,juga):
        i=0
        while i<len(self.__contrato) and str.lower(juga)!=str.lower(self.__contrato[i].jugador.DNI()):
            i=i+1
        if i<len (self.__contrato):
            print("{}{}".format(self.__contrato[i].equipo(),self.__contrato[i].fin()))
        else:
            print("No se encontro el contrato\n")
    def seismeses(self,equipo):
        i=0
        while i< len (self.__contrato) and str.lower(self.__contrato[i].equipo())!=str.lower(equipo):
            i=i+1
        if i<len(self.__contrato):
            hoy=datetime.now()
            for contrato in self.__contrato:
                if contrato.fin().find('/')!=-1:
                    auxfin=contrato.fin().split('/')
                    mes=auxfin[1]
                    if mes-hoy <6:
                        print(contrato)
    def guardar(self):
        archivo=open("Contratos.csv","w")
        write=csv.writer(archivo,delimiter=';')
        for contrato in self.__contrato:
            write.writerow(contrato)
    def importe(self,equipo):
        i=0
        while i<len(self.__contrato)and str.lower(self.__contrato[i].equipo.nombre()) !=str.lower(equipo):
            i=i+1
        if i<len(self.__contrato):
            for contrato in self.__contrato:
                if str.lower(contrato.equipo.nombre())==str.lower(equipo):
                    print(contrato)
