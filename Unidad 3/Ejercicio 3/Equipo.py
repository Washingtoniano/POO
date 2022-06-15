class equipo():
    __nombre=''
    __ciudad=''
    def __init__(self,nom,ci):
        self.__nombre=nom
        self.__ciudad=ci
    def nombre(self):
        return self.__nombre
