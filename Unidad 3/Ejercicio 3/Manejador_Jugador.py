import csv


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
            if band=False:


