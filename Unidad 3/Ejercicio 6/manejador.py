##se necesita una lista, un Manejador y un nodo
from interfaz import interfaz
from Lavarropas import Lavarropas
from Televisor import Televisor
from Heladera import Heladera
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

	def objeto(self):
		objeto=None
		print("Ingrese los datos del elemento\n")
		marca=input("Marca\n")
		modelo=input("Modelo\n")
		color=input("Color\n")
		pais=input("Pais\n")
		precio=float(input("Precio"))
		band=False
		clase=input("Tipo de aparato\n")
		while band!=True:
			if str.lower(clase)=='heladera':
				capacidad=input("La capacidad de la heladera\n")
				freezer=bool(int(input("Posee freezer?\n 0-No\t 1-Si")))
				ciclica=bool(int(input("Es ciclica?\n 0-No\t 1-Si")))
				print(freezer)
				print(ciclica)
				unaheladera=Heladera(marca,modelo,color,pais,precio,capacidad,freezer,ciclica)
				objeto=unaheladera
				band=True
			elif str.lower(clase)=='televisor':
				pantalla=input("Tipo de pantalla\n")
				pulgadas=input("Pulgadas\n")
				definicion=input("Definicion\n")
				internet=bool(input("Posee internet?\n 0-No\t 1-Si"))
				print(internet)
				untelevisor=Televisor(marca,modelo,color,pais,precio,pantalla,pulgadas,definicion,internet)
				objeto=untelevisor
				band=True
			elif str.lower(clase)=='lavarropas':
				capacidad=input("Ingrese la capacidad del lavarropas")
				velocidad=input("Velocidad de centrifugado")
				programas=int(input("Cantidad de programas"))
				tipodecarga=input("Tipo de carga")
				unlavarropas=Lavarropas(marca,modelo,color,pais,precio,capacidad,velocidad,programas,tipodecarga)
				objeto=unlavarropas
				band=True
			else:
				print("elemento no valido")
				clase=input("Tipo de aparato\n")
		return  (objeto)
	def opcion2(self):
		ob=self.objeto()
		if ob!=None:
			self.agregar_elemento(ob)

	def opcion1(self):
		ob=self.objeto()
		if ob!=None:
			pos=int(input("Por favor ingrese la posicion en la que quiere que este el objeto\n"))
			unnodo=nodo(ob)
			try:
				self.insertar_elemento(unnodo,pos)
			except IndexError:
				print ("El valor se salio de rango")
	def opcion3(self):
		po=input("ingrese la posicion que desea buscar")
		self.mostrar_elemento(po)
	def opcion4(self):
		aux=self.__com
		i=0
		print(type(aux.getDato()))
		print(aux.getDato())
		while aux!=None:
			print(type(aux.getDato.marca()))
			if str.lower(aux.getDato.marca())=='philips':

				print (aux.getDato())
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
			aux=aux.getSiguiente()
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
			self.opcion4()
		elif op==5:
			self.opcion5()
		elif op==6:
			self.opcion6()
		elif op==7:
			self.opcion7()
		else:
			print("Error")
