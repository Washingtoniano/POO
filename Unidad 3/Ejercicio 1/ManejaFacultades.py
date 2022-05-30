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
                    listaCarrera.append(fila)
                else:
                    nuevafacultad=Fac(facu[0],facu[1],facu[2],facu[3],facu[4],listaCarrera)
                    self.__indice.append(nuevafacultad)
                    listaCarrera=[]
                    facu=fila
        archivo.close()
    def opcion3(self):
        for facu in self.__indice:
            print(facu)
            for car in facu.getCarrera():
                print(car)
    def opcion1(self):
        i=0
        cod=int(input("Ingrese el codigo de la facultad"))
        while i<len(self.__indice)and self.__indice[i].getCodigo()!=cod:
            print(type(self.__indice[i].getCodigo()))
            i=i+1
        if i<len(self.__indice):
            print(self.__indice[i])
            print(self.__indice[i].getDuracion())
        else:
            print("error")
    def opcion2(self):
        nombre=input("Ingrese nombre de la carrera\n")
        i=0
        j=0
        car=None
        band=False
        while i< len(self.__indice) and band==False:
            car=self.__indice[i].getCarrera()
            print((car[j]))
            while(j<len(car) and car[j].getNombre!=nombre):
                j=j+1
            if j< len(car):
                j=0
                i=i+1
            else:
                band=True
        if band==True:
            print("codigo:{}{}-Nombre:{}-Localidad:{}".format(self.__indice[i].getCodigo(),car[j].getcodigo(),self.__indice[i].getNombre(),self.__indice[i].getLocalidad()))
        else:
            print("La carrera no se dicta en ninguna facultad")


