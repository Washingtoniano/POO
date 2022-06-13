class ramo():
    __cantidad=0
    __lista=[]
    def __init__(self,cantidad,arre=None,distintas=None):
        self.__cantidad=cantidad
        from Flores import flores
        if distintas==None:
            self.__lista=None
            self.__flor=flores(arre.id(),arre.nombre(),arre.color(),arre.descripcion())
        else:
            for element in distintas:
                self.__flor=flores(element.id(),element.nombre(),element.color(),element.descripcion())
                self.__lista.append(self.__flor)
    def cantidad(self):
        return self.__lista
    def lista(self):
        return self.__lista
    def flor(self):
        return self.__flor
