from Ramo import ramo
import numpy as np
class ManejadorR():
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def opcion1(self,arre):
        i=0
        cant=int(input("Por favor ingrese la cantidad de flores que llevara el ramo\n"))
        band=int(input("Seran todas del mismo tipo\n 1-Si\t 2-No"))

        if band ==1:
            tipo=int(input("Por favor ingrese el id de las flores que llevara el ramo\n"))
            print(type(arre[0]))
            while i< len(arre) and arre[i].id()!=tipo:
                i+=1
            if i<len(arre):
                unramo=ramo(cant,arre[i])
                self.__lista.append(unramo)
            else:
                print("flor no encontrada")
        else:
            aux=cant
            distintas=int(input("Debido a que selecciono mas de un tipo de flor, por favor ingre la cantidad de flores distintas, seguido de sus respectivos id"))
            tipos=np.empty(distintas,dtype=int)
            j=0
            list=[]
            while j< len (tipos):
                va=int(input("Ingrese el id de la flor numero",j+1))
                tipos[j]=va
                j=j+1

            while i<len(arre):
                while j<len(tipos):
                    if arre[i].id()==tipos[j]:
                        uno=(arre[i])
                        list.append(uno)
                    j+=1
                j=0
                i+=1

            unramo=ramo(cant,None,list)
            self.__lista.append(unramo)
    def opcion2(self):
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
            else:
                if element.cantidad()>max2:
                    max2=element.cantidad()
                    aux2=element.lista()
                    i=0
                    j=0
                    if lista==None:
                        while i<len(aux2):
                            lista.append(aux2[i])
                    else:
                        aux=lista
                        while j<len(aux2):

                            while i< len (aux):
                                if aux[i]==aux2[j]:
                                    j=j+1
                                else:
                                    aux.append(aux2[j])
                            j=0
                            i+=1

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
                    print(self.__lista[i].lista())
                    cant-=1
            i+=1









