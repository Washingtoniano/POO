from Ramo import ramo
import numpy as np
class ManejadorR():
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def opcion1(self,arre):
        i=0
        cant=int(input("Por favor ingrese la cantidad de flores que llevara el ramo(Pequeño:1-5 Mediano:6-10 Grande:11 o mas)\n"))
        while cant<=0:
            print("Es cantidad es imposible")
            cant=int(input("Por favor ingrese la cantidad de flores que llevara el ramo(Pequeño:1-5 Mediano:6-10 Grande:11 o mas)\n"))
        band=int(input("Seran todas del mismo tipo\n 1-Si\t 2-No"))
        if band ==1:
            tipo=int(input("Por favor ingrese el id de las flores que llevara el ramo\n"))
            while i< len(arre) and arre[i].id()!=tipo:
                i+=1
            if i<len(arre):
                unramo=ramo(cant,arre[i])
                self.__lista.append(unramo)
            else:
                print("flor no encontrada")
        else:

            p=int(input("Debido a que selecciono mas de un tipo de flor, la cantidad total de flores del ramo seran{}, ahora necesitamos saber los distintos tipos deflores que desea, para ello por favor ingrese dicha cantidad, seguido de los ide las mismas".format(cant)))
            tipos=np.empty(p,dtype=int)

            a=0
            list=[]
            print(len(tipos))
            for j in range( len (tipos)):

                va=int(input("Ingrese el id de la flor numero {}".format(j+1)))
                tipos[j]=va
            print (tipos)

            for i in range(len(arre)):
                for j in range(len(tipos)):
                    if arre[i].id()==tipos[j]:
                        uno=(arre[i])
                        list.append(uno)
            unramo=ramo(cant,None,list)
            self.__lista.append(unramo)
    def opcion2(self):
        band=False
        max1=0
        max2=0
        aux1=None
        aux2=None
        lista=[]
        for element in self.__lista:
            if element.lista()==None:
                if element.cantidad()>max1:
                    max1=element.cantidad()
                    aux1=element.flor()
                    lista.append(aux1)
                    band=True
            else:
                if element.cantidad()>max2:
                    max2=element.cantidad()
                    aux2=element.lista()
                    i=0
                    j=0
                    band=True
                    if lista==None:
                        lista=aux2
                    else:
                        while j<len(aux2):
                            while i< len (lista):
                                if lista[i]==aux2[j]:
                                    i=i+1
                                else:
                                    lista.append(aux2[j])
                                    i+=1
                            i=0
                            j+=1
        if band==True:
            print ("Las 5 flores mas pedidas son\n")
            cant=5
            i=0
            while cant!=0 and i< len(self.__lista):
                if self.__lista[i].lista()==None:
                    if self.__lista[i].cantidad()==max1:
                        print(self.__lista[i].flor())
                        cant-=1
                else:
                    if self.__lista[i].cantidad()==max2:

                        for element in self.__lista[i].lista():
                            print(element)
                        cant-=1
                i+=1
        else:
            print("No hay ramos cargados")
    def opcion3(self):
        band=False
        tamano=str.lower(input("Por favor ingrese el tamaño de los ramos que desea buscar\n"))
        for element in self.__lista:
            if element.tamano()==tamano:
                print(element)
                band=True
        if band==False:
            print("No se encontraron ramos de cuyo tamaño sea",tamano)

    def list(self):
        return self.__lista










