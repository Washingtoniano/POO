import csv
from Facultad import Fac
class ManejaFacultades():
    __lista=[]
    def __init__(self):
        self.__indice=[]
    def leer(self):
        archivo=open("Facultades.csv","r")
        reader=csv.reader(archivo,delimiter=';')
        band=True
        facu=None
        listaCarrera=None
        for fila in reader:
            if band==True:
                band=False
                facu=fila
                listaCarrera=[]
            else:
                if fila[0]==facu[0]:
                    listaCarrera.append(facu)
                else:
                    nuevafacultad=Fac(facu[0],facu[1],facu[2],facu[3],facu[4],listaCarrera)
                    self.__indice.append(nuevafacultad)
                    listaCarrera=[]
                    facu=fila
        archivo.close()
    def mostrar(self):
        for facu in self.__indice:
            print(facu)
