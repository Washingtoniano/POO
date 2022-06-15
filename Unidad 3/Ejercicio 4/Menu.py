from Coleccion import coleccion
class menu():

    def __init__(self,ca):
        self.__coleccion=coleccion(ca)
        self.__coleccion.leer()
    def manejador(self,op):
        if op>=1 and op<4:
            self.__coleccion.opcion3(op)
        else:
            print("error")
