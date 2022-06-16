from Personal import personal
class Apoyo():
    __categoria=''
    def __init__(self,cuil,apellido,nombre,sueldo,antiguedad,categoria):
        super.__init__(cuil,apellido,nombre,sueldo,antiguedad)
        self.__categoria=categoria
