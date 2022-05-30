##se necesita una lista, un Manejador y un nodo
@implementer(interfaz)
from nodo import nodo
class manejador:
	__com=None
	def __init__ (self, objeto):
		self.__com=None
	def agregar_elemento(self,objeto)
		nodo=nodo(objeto)
		nodo.setSiguiente(self.__com)
		self.__com=nodo
	def insertar_elemento(self,objeto,pos):
		##objeto es un nodo ,recomendacion: inicializar el nodo apuntando a siguiente None"
		rto=False
		if self.__com==None:
			self.__com=objeto
			rto=True
		if pos==0:
			objeto.setSiguiente(self.__com.getSiguiente)
			self.__com=objeto
			rto=True
		else:
			aux=self.__com
			i=0
			while  i<pos and aux.getSiguienre!=None :
				i=i+1
				aux=aux.getSiguiente()
			if i<= pos:
	
				objeto.setSiguiente(aux.getSiguiente)
				aux.setSiguiente(nuevo)
				rto=True
			else:
				 rto=False
			return rto
	def mostrar_elemento(self,pos):
	if pos=0:
		print(self.__com)
	else:
		i=0
		aux=self.__com
		while i<len (pos) and aux.getsiguiente!=None:
			i=i+1
		if aux.getSiguiente==None:
			print("No hay valor para esa posicion")
		else:
			print(aux)


	def opcion1(self):
		self.agregar_elemento()
	def opcion2(self):
		self.insertar_elemento()
	def opcion3(self):
		po=input("ingrese la posicion que desea buscar")
		self.mostrar_elemento(op)
	def opcion4(self):
	def opcion5(self):
	def opcion6(self):
	def opcion7(self):
