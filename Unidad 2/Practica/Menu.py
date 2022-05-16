from ManejadorLugar import ML
from ManejadorInscripto import MI
class menu():
    __IndiceMI=MI()
    __IndiceML=ML()
    def __init__(self):
        self.__IndiceML=ML()
        self.__IndiceMI=MI()
    def inicalizar(self):
        self.__IndiceML.leer()
        self.__IndiceMI.leer()
        self.__IndiceMI.calcular()
    def manejador(self,op):
        if op==1:
            self.opcion1()
        elif op==2:
            self.opcion2()
        elif op==3:
            self.opcion3()
        else:
            print("Opcion no valida")
    def opcion1(self):
        self.__IndiceMI.opcion1()
    def opcion2(self):
        self.__IndiceMI.opcion2()
    def opcion3(self):
        self.__IndiceMI.mostrar()

