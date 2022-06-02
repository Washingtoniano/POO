from Aparatos import aparatos
class Heladera(aparatos):
    __capacidad=''
    __freezer=bool
    __ciclica=bool
    def __init__(self,marca,modelo,color,pais,precio,capacidad,freezer,ciclica):
        super().__init__(marca,modelo,color,pais,precio)
        self.__ciclica=ciclica
        self.__freezer=freezer
        self.__capacidad=capacidad
    def importe(self):
        monto=super().monto()
        total=monto
        if self.__ciclica==True:
            total=total+monto*10/100
        if self.__freezer==True:
            total=total+monto*5/100
        else:
            total=total+monto*1/100
        return total+monto
