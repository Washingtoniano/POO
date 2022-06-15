from Manejador_equipo import ME
from Manejador_Jugador import MJ
from Manejador_contrato import MC
class menu():
    __Me=ME(1)
    __Mj=MJ()
    __Mc=MC(1)
    def __init__(self):
        self.__Mj=MJ()
        self.__Mc=MC(1)
        self.__Me=ME(1)
        self.__dimension=self.__Me.dimension()
        self.__indice=self.__Mj.indice()
    def operador(self,op):
        if op==1:
            self.opcion1()
        elif op==2:
            self.opcion2()
        elif op==3:
            self.opcion3()
        elif op==4:
            self.opcion4()
        elif op==5:
            self.opcion5()
        else:
            print("Error")
    def opcion1(self):
        self.__Me.leer()

        self.__Mj.leer()

    def opcion2(self):
        self.__Mc.leer(self.__dimension,self.__indice)
    def opcion3(self):
        juga=input("Ingrese el DNI del jugador\n")
        self.__Mc.consultar(juga)
    def opcion4(self):
        equipo=input ("Ingrese el nombre del equipo\n")
        self.__Mc.seismeses(equipo)
    def opcion5(self):
        equipo=input("ingrese el equipo que desea")
        self.__Mc.importe(equipo)
    def opcion6(self):
        self.__Mc.guardar()
