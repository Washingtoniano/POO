class nodo:
	elemento=None
	siguiente=None
	def __init__ (self,elemento):
		self.__elemento=elemento
		self.__siguiente=None
	def setSiguiente(self,siguiente):
		self.__siguiente=siguiente
	def getSiguiente (self):
		return(self.__siguiente)
	def getDato(self):
		return (self.__elemento)
