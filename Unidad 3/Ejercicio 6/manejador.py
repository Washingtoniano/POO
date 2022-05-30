##se necesita una lista, un anejador y un nodo
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
			self.__com=
			rto=True
		else:
			aus=self.__com
			i=0
			while aux.getSiguienre!=None and i<pos:
				i=i+1
				aux=aux.getSiguiente()
			if i<= pos:
	
				objeto.setSiguiente(aux.getSiguiente)
				aux.setSiguiente(nuevo)
				rto=True
			else:
				 rto=False
			return rto
	def mostrar_elemento(self,pos)
	if pos=0
	
				