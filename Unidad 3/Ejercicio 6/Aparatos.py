class aparatos():
    __marca=''
    __modelo=''
    __color=''
    __pais=''
    __precio=0.0
    def __init__(self,marca,modelo,color,pais,precio):
        self.__pais=pais
        self.__color=color
        self.__precio=precio
        self.__modelo=modelo
        self.__marca=marca
    def monto(self):
        return float(self.__precio)
    def marca(self):
        return (self.__marca)
    def __str__(self):
        return("Marca:{}-Pais:{}-Importe:{}\n".format(self.__marca,self.__pais,self.__precio))
    