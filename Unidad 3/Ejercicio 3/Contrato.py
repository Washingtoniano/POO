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
    def jugador(self):
        return self.__jugador
    def equipo(self):
        return self.__equipo.nombre()
    def fin(self):
        return self.__fin
    def __str__(self):
        return ("Inicio:{}-FIn:{}-Pago:{}-Equipo:{}-Jugador:{}".format(self.__inicio,self.__fin,self.__pago,self.__equipo,self.__jugador))
