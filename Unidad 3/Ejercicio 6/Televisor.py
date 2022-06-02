from copyreg import pickle
from Aparatos import aparatos
import json
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
    def importe(self):
        total=0
        monto= super().monto()
        if self.__definicion=='SD':
            total=total+monto*1/100
        elif self.__definicion== 'HD':
            total=total+monto*2/100
        elif self.__definicion== 'FULL HD':
            total=total+monto*3/100
        if self.__internet== True:
            total=total+monto*10/100
        return total+monto
    def toJason(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                color=self.__color,
                pantalla=self.__pantalla,
                pulgadas=self.__pulgadas,
                interntet=self.__internet,
                definiicion=self.__definicion,
                marca=self.__marca,
                modelo=self.__modelo,
                pais=self.__pais,
                precio=self.__precio

            )
        )
        return d