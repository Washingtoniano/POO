import csv

from Inscripto import Persona
class MI():
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def leer (self):
        archivo=open("inscriptos20210503.csv",'r')
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                unincripto=Persona(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
                self.__lista.append(unincripto)
        archivo.close()

    def opcion1(self):

        for persona in self.__lista:
            cant=0
            cantF=0
            for per in self.__lista:
                if persona.edad()==per.edad():
                    if per.riesgo()=='Ninguno':
                        cant=cant+1
                    else:
                        cantF+=1
            print ("Para la edad de {} existen {} personas con factor de riesgo y {} personas sin factor de riesgo".format(persona.edad(),cantF,cant))
    def opcion2(self):
        zona=input("Ingrese el nombre de l zona a buscar\n")
        nuevo=[]
        for i in range (len(self.__lista)):
            if str.lower(self.__lista[i].zona())==str.lower(zona):
               nuevo.append(self.__lista[i])
        j=0
        while j < len(nuevo) and j+1<len(nuevo):
            if nuevo[j+1]>nuevo[j]:
                aux=nuevo[j]
                nuevo[j]=nuevo[j+1]
                nuevo[j+1]=aux
            print (nuevo[j])
            j+=1
    def mostrar(self):
        for persona in self.__lista:
            print (persona)
    def calcular(self):
        for i in range(len(self.__lista)):
            va=0

            if self.__lista[i].riesgo()=='Obesidad' or self.__lista[i].riesgo()=='Diabetes':
                va=va+50


            elif self.__lista[i].riesgo()=='Renal' or self.__lista[i].riesgo()=='Respiratoria' or self.__lista[i].riesgo()=='Cardiovascular':
                va=va+40

            elif  self.__lista[i].riesgo()=='Cirrosis' or self.__lista[i].riesgo()=='HIV':
                va=va+30
            self.__lista[i].sumar(va)


            
