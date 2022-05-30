from Aparatos import aparatos
class Televisor(aparatos):
    __pantalla=''
    __pulgadas=''
    __definicion=''
    __internet=bool
    def __init__(self,marca,modelo,color,pais,precio,pantalla,pulgadas,definicion,internet):
        super().__init__(marca,modelo,color,pais,precio)
        self.__pantalla=pantalla
        self.__internet=internet
        self.__definicion=definicion
        self.__pulgadas=pulgadas

