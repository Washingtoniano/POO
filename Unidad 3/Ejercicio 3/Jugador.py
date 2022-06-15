class jugador():
    __nombre=''
    __dni=0
    __Ciudad=''
    __Pais=''
    __naci=''
    __conta=[]
    def __init__(self,nom,Dni,ciu,pa,Na):
        self.__nombre=nom
        self.__dni=Dni
        self.__Ciudad=ciu
        self.__Pais=pa
        self.__naci=Na
        self.__conta=[]
    def nombre(self):
        return self.__nombre
    def __str__(self):
        return("Nombre:{}-DNI:{}-Ciudad:{}-Pais:{}-Nacionalidad:{}-Contratos:{}\n".format(self.__nombre,self.__dni,self.__Ciudad,self.__Pais,self.__naci,self.__conta))
    def contratar(self,contra):
        self.__conta.append(contra)
    def DNI(self):
        return self.__dni
