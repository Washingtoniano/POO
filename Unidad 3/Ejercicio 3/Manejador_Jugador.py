import csv
from Jugador import jugador

class MJ():
    __indice=[]
    def __init__(self):
        self.__indice=[]
    def leer (self):
        #crear archivo de prueba
        archivo=open("Jugadores.csv",'r')
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                unjugador=jugador(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__indice.append(unjugador)
    def mostrar(self):
        for ele in self.__indice:
            print(ele)
    def indice(self):
        return self.__indice

