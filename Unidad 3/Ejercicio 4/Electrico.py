class electrico():
    __potenciamax=0
    __calecator=None
    def __init__(self,marca,modelo,potenciamas):
        self.__potenciamax=potenciamas
        from Calefactor import calefactor
        uncalefactor=calefactor(marca,modelo)
        self.__calecator=uncalefactor
    def consumo(self):
        return int(self.__potenciamax)
    def marca(self):
        return self.__calecator.marca()
    def modelo(self):
        return self.__calecator.modelo()
    def __str__(self):
        return("Tipo: Electrico-Marca:{}-Modelo:{}-PotenciaMax:{}".format(self.__calecator.marca(),self.__calecator.modelo(),self.__potenciamax))
