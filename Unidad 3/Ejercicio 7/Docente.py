from Personal import personal
class Docente():
    __carrera=''
    __cargo=''
    __catedra=''
    def __init__(self,cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra):
        super.__init__(cuil,apellido,nombre,sueldo,antiguedad)
        self.__cargo=cargo
        self.__carrera=carrera
        self.__catedra=catedra

