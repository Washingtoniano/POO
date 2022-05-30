class Fac():
	__codigo=int
	__nombre=str
	__direccion=str
	__localidad=str
	__telefono=int
	__Carrera=[]
	def __init__(self,cod,nombre,direccion,localidad,telefono,lista):
		from carrera import Carrera
		self.__codigo=cod
		self.__nombre=nombre
		self.__direccion=direccion
		self.__localidad=localidad
		self.__telefono=telefono
		self.__Carrera=[]
		for i in range (len(lista)):
			unacarrera=Carrera(lista[i][0],lista[i][1],lista[i][2],lista[i][3])
			self.__Carrera.append(unacarrera)
	def getCodigo(self):
		return(self.__codigo)
	def getDireccion(self):
		return(self.__direccion)
	def getLocalidad (self):
		return(self.__localidad)
	def getTelefono(self):
		return(self.__telefono)
	def getCant (self):
		return(self.__cantMaterias)
	def __str__(self):
		return ("Codigo:{}-Facultad:{}-Direccion:{}-Localidad:{}-Telefono:{}".format(self.__codigo,self.__nombre,self.__direccion,self.__localidad,self.__telefono))
	def mostrar (self):
		for carrera in self.__Carrera:
			print (carrera)
