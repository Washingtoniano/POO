from Docente import Docente
from Investigador import inverstigador
class DI():
    __categoria=''
    __extra=''
    def __init__(self,cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra,area,tipo,categoria,extra):
        inverstigador.__init__(cuil,apellido,nombre,sueldo,antiguedad,area,tipo)
        Docente.__init__(cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra)
        self.__categoria=categoria
        self.__extra=extra
