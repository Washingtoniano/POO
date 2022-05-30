from Manejador_equipo import ME
from Manejador_Jugador import MJ
from Manejador_contrato import MC
class menu():
    __Me=ME(10)
    __Mj=MJ()
    __Mc=MC(10)
    def __init__(self):
        self.__Mj=MJ()
        self.__Mc=MC(10)
        self.__Me=ME(10)

