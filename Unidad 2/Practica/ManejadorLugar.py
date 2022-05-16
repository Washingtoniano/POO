import csv

from Lugar import lugar
class ML():
    __indice=[]
    def __init__(self):
        self.__indice=[]
    def leer (self):
        archivo=open("lugaresVac.csv",'r')
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                unlugar=lugar(fila[0],fila[1])
                self.__indice.append(unlugar)
    
