class flores():
    __numero=0
    __nombre=''
    __color=''
    __descripcion=''
    def __init__(self,numero,nombre,color,descripcion):
        self.__color=color
        self.__numero=numero
        self.__nombre=nombre
        self.__descripcion=descripcion
    def id(self):
        return int(self.__numero)
    def nombre(self):
        return (self.__nombre)
    def color(self):
        return (self.__color)
    def descripcion(self):
        return self.__descripcion
    def __eq__(self, other):
        return self.__numero==other.__numero
    def __ne__(self, other):
        return self.__numero!=other.__numero
