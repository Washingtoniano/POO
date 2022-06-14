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
            self.__MR.opcion3()
        elif op==5:
            print("lista flores")
            for uno in self.__dimension:
                print (uno)
        elif op==6:
            print("lista de ramos")
            for uno in self.__MR.list():
                print (uno)
        else:
            print("opcion no valida")

