
from Menu import  menu
if __name__ == '__main__':
    ca=int(input("Ingrese la cantidad del arreglo"))
    unmenu=menu(ca)
    op=int(input("Seleccione la opcion que desea\n1-Ingresar por teclado el  costo por m3 y cantidad que se estima consumir en m3 y mostrar marca y modelo del calefactor a gas natural de menor costo de consumo.\n2-Ingresar por teclado el costo de el kilowatt/h, la cantidad que se estima consumir por hora y mostrar  marca  y modelo del calefactor eléctrico de menor consumo.\n3-Teniendo en cuenta los dos ítems anteriores, muestre: tipo de calefactor y todos los datos del calefactor de menor consumo."))
    while op!=4:
        unmenu.manejador(op)
        op=int(input("Seleccione la opcion que desea\n1-Ingresar por teclado el  costo por m3 y cantidad que se estima consumir en m3 y mostrar marca y modelo del calefactor a gas natural de menor costo de consumo.\n2-Ingresar por teclado el costo de el kilowatt/h, la cantidad que se estima consumir por hora y mostrar  marca  y modelo del calefactor eléctrico de menor consumo.\n3-Teniendo en cuenta los dos ítems anteriores, muestre: tipo de calefactor y todos los datos del calefactor de menor consumo."))
    print("Adios")
