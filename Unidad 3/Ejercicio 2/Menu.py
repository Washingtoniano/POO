from Manejador_Ramos import ManejadorR
from Manejador_Flores import ManejadorF
class menu():
    __MR=ManejadorR()
    __MF=ManejadorF()
    def inicializador(self):
        self.__MF.leer()
        self.__dimension=self.__MF.dimension()
    def manejador(self,op):
        if op==1:
            self.__MR.opcion1(self.__dimension)
        elif op==2:
            self.__MR.opcion2()
        elif op==3:
            self.__MR.opcion3(self.__dimension)
        else:
            print("opcion no valida")
