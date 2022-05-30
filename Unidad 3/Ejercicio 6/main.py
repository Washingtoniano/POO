from Menu import menu
import os
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
    return band

if __name__ == "__main__":
    band=False
    unmenu=menu()
    op=(input("seleccione la opcion que desea realizar\n1-Insertar un aparato en la colección en una posición determinada.\n2-Agregar un aparato a la colección (solicitar el tipo de aparato, y luego los datos que correspondan).\n3-Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.\n4-Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips.\n5-Mostrar la marca de todos los lavarropas que tienen carga superior .\n6-Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta.\n7-Almacenar los objetos de la colección Lista en el archivo “aparatoselectronicos.json”."))
    while band!=True and op!='8':
        band=True
        op=(input("seleccione la opcion que desea realizar\n1-Insertar un aparato en la colección en una posición determinada.\n2-Agregar un aparato a la colección (solicitar el tipo de aparato, y luego los datos que correspondan).\n3-Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.\n4-Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips.\n5-Mostrar la marca de todos los lavarropas que tienen carga superior .\n6-Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta.\n7-Almacenar los objetos de la colección Lista en el archivo “aparatoselectronicos.json”."))
        band=testBloqueTryExcept(op)
        if band==True:
            unmenu.operador(int(op))
        else:
            os.system('cls')

