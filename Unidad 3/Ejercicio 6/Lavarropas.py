from Aparatos import aparatos
import json
class Lavarropas(aparatos):
    __capacidad=''
    __velocidad=''
    __programas=0
    __tipodecarga=''
    def __init__(self,marca,modelo,color,pais,precio,capapacidad,velocidad,programas,tipo):
        super().__init__(marca,modelo,color,pais,precio)
        self.__capacidad=capapacidad
        self.__velocidad=velocidad
        self.__programas=programas
        self.__programas=programas
        self.__tipodecarga=tipo
    def monto (self):
        total=0
        monto=super().monto()
        if int(self.__capacidad)<=5:
            total=total+monto*1/100
        else:
            total=total+monto*3/100
        return total+monto
    def carga(self):
        return self.__tipodecarga