from Personal import personal
class inverstigador():
    __area=''
    __tipo=''
    def __init__(self,cuil,apellido,nombre,sueldo,antiguedad,area,tipo):
        personal.__init__(cuil,apellido,nombre,sueldo,antiguedad)
        self.__tipo=tipo
        self.__area=area
