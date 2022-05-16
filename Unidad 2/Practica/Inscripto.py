class Persona():
    __apellido=''
    __nombre=''
    __DNI=0
    __edad=0
    __Telefono=0
    __zona=''
    __riesgo=''
    __riesgoP=0
    def __init__(self,apellido,nombre,dni,edad,telefono,zona,riesgo='Ninguno'):
        self.__apellido=apellido
        self.__nombre=nombre
        self.__DNI=dni
        self.__edad=edad
        self.__Telefono=telefono
        self.__zona=zona
        self.__riesgo=riesgo
    def edad(self):
        return self.__edad
    def riesgo(self):
        return self.__riesgo
    def zona(self):
        return self.__zona
    def sumar (self,va):
        self.__riesgoP=self.__riesgoP+va
    def riesgoP(self):
        return self.__riesgoP

    def __str__(self):
        return("Apellido:{}-Nombre:{}-DNI:{}-Telefono:{}-Puntaje:{}-Zona:{}".format(self.__apellido,self.__nombre,self.__DNI,self.__Telefono,self.__riesgoP,self.__zona))
    def __gt__(self, other):
        return self.__riesgoP>other.__riesgoP
