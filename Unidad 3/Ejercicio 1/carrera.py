class Carrera():
	__codigo=0
	__Nombre=''
	__Duracion=''
	__Inicio=''
	__codFac=0
	__titulo=''
	def __init__(self,codFac,codigo,Nombre,inicio,Duracion,titulo):
		self.__codFac=codFac
		self.__codigo=codigo
		self.__Nombre=Nombre
		self.__Duracion=Duracion
		self.__Inicio=inicio
		self.__titulo=titulo

	def getDuracion(self):
		return self.__Duracion
	def getcodigo (self):
		return(self.__codigo)
	def getDuracion(self):
		return (self.__Duracion)
	def getNombre(self):
		return (self.__Nombre)
	def getInicio(self):
		return (self.__Inicio)
	def __str__(self):
		return ("Codigo:{}-Nombre:{}-Duracion:{}-Inicio:{}".format(self.__codigo,self.__Nombre,self.__Duracion,self.__Inicio))
