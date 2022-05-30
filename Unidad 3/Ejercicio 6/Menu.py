from manejador import manejador
class menu():
    __man=manejador
    def __init__(self,objeto):
        self.__man=manejador(objeto)
    def operador(self,op):
        if op==1:
            self.__man.opcion1()
        elif op==2:
            self.__man.opcion2()
        elif op==3:
            self.__man.opcion3()
        elif op==4:
            self.__man.opcion4()
        elif op==5:
            self.__man.opcion5()
        elif op==6:
            self.__man.opcion6()
        elif op==7:
            self.__man.opcion7()
        else:
            print("Error")
