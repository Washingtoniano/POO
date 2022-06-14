class ramo():
    __cantidad=0
    __tamano=''
    __lista=[]
    def __init__(self,cantidad,arre=None,distintas=None):
        self.__cantidad=cantidad
        if cantidad>=1 and cantidad<=5:
            self.__tamano='pequeño'
        elif cantidad>5 and cantidad<=10:
            self.__tamano='mediano'
        else:
            self.__tamano='grande'

        from Flores import flores
        if distintas==None:
            self.__lista=None
            self.__flor=flores(arre.id(),arre.nombre(),arre.color(),arre.descripcion())
        else:
            for element in distintas:
                self.__flor=flores(element.id(),element.nombre(),element.color(),element.descripcion())
                self.__lista.append(self.__flor)
    def cantidad(self):
        return self.__cantidad
    def lista(self):
        return self.__lista
    def flor(self):
        return self.__flor
    def tamano(self):
        return self.__tamano
    def __eq__(self, other):
        return (self.__tamano==other.__tamano)
    def __str__(self):
        element=None
        if self.__lista==None:
            element=("Cantidad de flores:{}-Tamaño:{}-Tipo de flor:{}".format(self.__cantidad,self.__tamano,self.__flor))
        else:
            element=("Cantidad de flores:{}-Tamaño:{}-Tipo de flores:{}".format(self.__cantidad,self.__tamano,self.__lista))
        return element

