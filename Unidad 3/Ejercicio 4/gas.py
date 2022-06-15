class gas():
    __matricula=''
    __calorias=0
    __calecator=None
    def __init__(self,marca,modelo,matricula,calorias):
        self.__matricula=matricula
        self.__calorias=calorias
        from Calefactor import calefactor
        uncalefactor=calefactor(marca,modelo)
        self.__calecator=uncalefactor
    def consumo(self):
        return int(self.__calorias)
    def marca(self):
        return self.__calecator.marca()
    def modelo(self):
        return self.__calecator.modelo()
    def __str__(self):
        return("Tipo: Gas-Marca:{}-Modelo:{}-Matricula:{}-Calorias:{}".format(self.__calecator.marca(),self.__calecator.modelo(),self.__matricula,self.__calorias))
