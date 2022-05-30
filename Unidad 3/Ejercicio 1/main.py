from ManejaFacultades import ManejaFacultades
from Menu import Menu
if __name__ =="__main__":
	unmenu=Menu()
	unmenu.inicializar()
	op=int(input("Seleccione la opcion que desea\n1-Buscar facultad por codigo\t2-Buscar carrera\t3-Mostrar\n"))
	while op!=4:
		unmenu.manejador(op)
		op=int(input("Seleccione la opcion que desea\n1-Buscar facultad por codigo\t2-Buscar carrera\t3-Mostrar\n"))

