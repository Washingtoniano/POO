class contrato():
    __inicio=''
    __fin=''
    __pago=0.0
    __jugador=None
    __equipo=None
    def __init__(self,Ini,fin,pago,equipo,jugador):
        self.__inicio:Ini
        self.__fin=fin
        self.__pago=pago
        self.__equipo=equipo
        self.__jugador=jugador
