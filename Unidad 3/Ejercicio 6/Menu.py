from ManejaFacultades import ManejaFacultades
class Menu():
    __MF=ManejaFacultades
    def __init__(self):
        self.__MF=ManejaFacultades()
    def inicializar(self):
        self.__MF.leer()
    def manejador(self,op):
        if op==1:
            self.__MF.opcion1()
        elif op==2:
            self.__MF.opcion2()
        elif op==3:
            self.__MF.opcion3()
