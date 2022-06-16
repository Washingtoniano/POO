from interfaz import interfaz
from nodo import nodo
from Docente import Docente
from Apoyo import Apoyo
from Investigadro import investigador
from zope.interface import implementer
@implementer(interfaz)
class manejador:
	__com=None
	def __init__ (self):
		self.__com=None
	def agregar_elemento(self,objeto):
		unnodo=nodo(objeto)
		unnodo.setSiguiente(self.__com)
		self.__com=unnodo
	def insertar_elemento(self,objeto,pos):
		##objeto es un nodo ,recomendacion: inicializar el nodo apuntando a siguiente None"
		if self.__com==None:
			self.__com=objeto
		if pos==0:
			objeto.setSiguiente(self.__com.getSiguiente())
			self.__com=objeto
		else:
			aux=self.__com
			i=0
			while  i<pos and aux!=None :
				i=i+1
				aux=aux.getSiguiente()
			if i== pos:
				objeto.setSiguiente(aux.getSiguiente())
				aux.setSiguiente(objeto)
			else:
				raise IndexError
	def mostrar_elemento(self,pos):
		if pos==0:
			print(self.__com)
		else:
			i=0
			aux=self.__com
			while i<len (pos) and aux!=None:
				i=i+1
			if aux.getSiguiente==None:
				print("No hay valor para esa posicion")
			else:
				print(aux)


