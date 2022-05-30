from Aparatos import aparatos
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
        self.__tipodecarga=tipo
