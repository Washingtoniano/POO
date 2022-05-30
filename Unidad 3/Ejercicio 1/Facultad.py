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
			unacarrera=Carrera(lista[i][0],lista[i][1],lista[i][2],lista[i][3],lista[i][4],lista[i][5])
			self.__Carrera.append(unacarrera)
	def getCodigo(self):
		return(int(self.__codigo))
	def getDireccion(self):
		return(self.__direccion)
	def getLocalidad (self):
		return(self.__localidad)
	def getTelefono(self):
		return(self.__telefono)
	def getCant (self):
		return(self.__cantMaterias)
	def getCarrera(self):
		return self.__Carrera
	def getNombre(self):
		return self.__nombre
	def getDuracion(self):
		for Carrera in self.__Carrera:
			print ("Carrera:{}-Duracion:{}".format(Carrera.getNombre(),Carrera.getDuracion()))
	def __str__(self):
		return ("Codigo:{}-Facultad:{}-Direccion:{}-Localidad:{}-Telefono:{}\n".format(self.__codigo,self.__nombre,self.__direccion,self.__localidad,self.__telefono))
	def mostrar (self):
		for carrera in self.__Carrera:
			print (carrera)
