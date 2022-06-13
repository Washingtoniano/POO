
from Menu import menu
def testBloqueTryExcept(op):
    try:
        int(op)<10
    except ValueError:
        print("Se ingreso un valor que no es un numero\n")
        va=input("Seleccione la opcion que desea\n 1-Registrar un ramo vendido\n 2-Las 5 flores mas vendidas\n 3-Ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño considerando todos los ramos vendidos\n 4-Salir\n")
        op=testBloqueTryExcept(va)
    return int(op)
if __name__ == '__main__':
    unmenu=menu()
    unmenu.inicializador()
    va=input("Seleccione la opcion que desea\n 1-Registrar un ramo vendido\n 2-Las 5 flores mas vendidas\n 3-Ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño considerando todos los ramos vendidos\n 4-Salir\n")
    op=testBloqueTryExcept(va)
    while(op!=4):
        op=testBloqueTryExcept(va)
        unmenu.manejador(op)
        va=input("Seleccione la opcion que desea\n 1-Registrar un ramo vendido\n 2-Las 5 flores mas vendidas\n 3-Ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño considerando todos los ramos vendidos\n 4-Salir\n")




