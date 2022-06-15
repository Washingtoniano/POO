from manejador import manejador
import os
##El iterador del json se realiza con un while o implementando ciertos metodos
#Para mostrar el dato debo pedirselo al nodo
def testBloqueTryExcept(op):
    try:
        int(op)<10
        band=True
    except SyntaxError:
        print("error de sintaxis valores incorrectos")
        band=False
    except ValueError:
        band=False
        print("error de sintaxis valores incorrectos")
    return int (op)

if __name__ == "__main__":
    band=False
    unmanejador=manejador()

    op=(input("seleccione la opcion que desea realizar\n1-Insertar un aparato en la colección en una posición determinada.\n2-Agregar un aparato a la colección (solicitar el tipo de aparato, y luego los datos que correspondan).\n3-Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.\n4-Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips.\n5-Mostrar la marca de todos los lavarropas que tienen carga superior .\n6-Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta.\n7-Almacenar los objetos de la colección Lista en el archivo “aparatoselectronicos.json”."))
    op=testBloqueTryExcept(op)
    while  op!=8:
        unmanejador.operador(op)

        os.system('cls')
        op=(input("seleccione la opcion que desea realizar\n1-Insertar un aparato en la colección en una posición determinada.\n2-Agregar un aparato a la colección (solicitar el tipo de aparato, y luego los datos que correspondan).\n3-Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.\n4-Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips.\n5-Mostrar la marca de todos los lavarropas que tienen carga superior .\n6-Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta.\n7-Almacenar los objetos de la colección Lista en el archivo “aparatoselectronicos.json”."))
        op=testBloqueTryExcept(op)
    print ("Adios")
