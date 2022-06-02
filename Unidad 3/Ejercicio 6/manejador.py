##se necesita una lista, un Manejador y un nodo
from Aparatos import aparatos
from interfaz import interfaz
from Lavarropas import Lavarropas
from nodo import nodo
import json
from zope.interface import implementer

@implementer(interfaz)
class manejador:
	__com=None
	def __init__ (self):
		self.__com=None
	def agregar_elemento(self,objeto):
		unnodo=nodo(objeto)
		unnodo.setSiguiente(self.__com)
		self.__com=nodo
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


	def opcion1(self):
		self.agregar_elemento()
	def opcion2(self):
		try:
			self.insertar_elemento()
		except IndexError:
			print ("El valor se salio de rango")
	def opcion3(self):
		po=input("ingrese la posicion que desea buscar")
		self.mostrar_elemento(po)
	def opcion4(self):
		aux=self.__com
		i=0
		while aux!=None:
			dato=aux.getDato()
			if str.lower(dato.marca())=='philips':
				print (dato)
				i=i+1
			aux=aux.getSiguiente()
		if i==0:
			print ("No hay electrodomesticos de la marca Phlips")
		else:
			print ("Poseemos",i,"elementos de la marca Philips")
	def opcion5(self):
		from Lavarropas import Lavarropas
		aux=self.__com
		i=0
		while aux!=None:
			if aux == Lavarropas:
				dato=aux.getDato()
				if str.lower(dato.carga())=='superior':
					i=i+1
					print (dato)
			aux=aux.getSiguiente()
		if i>0:
			print ("Existen",i,"lavarropas con carga supeior")
		else:
			print("No hay lavarropas de carga superior")

	def opcion6(self):
		aux=self.__com
		while aux!=None:
			print(aux.getDato())
	def toJason(self):
		d=dict(
			__class__=self.__class__.__name__,
			aparatos=[aparato.toJason() for aparato in self.__com ]
		)
		return d
	def opcion7(self):
		self.toJason()
	def operador(self,op):
		if op==1:
			self.opcion1()
		elif op==2:
			self.opcion2()
		elif op==3:
			self.opcion3()
		elif op==4:
			self.__man.opcion4()
		elif op==5:
			self.opcion5()
		elif op==6:
			self.opcion6()
		elif op==7:
			self.opcion7()
		else:
			print("Error")