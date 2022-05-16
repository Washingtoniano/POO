from Menu import menu
if __name__ == '__main__':
    unMenu=menu()
    unMenu.inicalizar()
    op=int (input("Seleecione la opcion deseada\n\t1-Listar Personas\t2-Buscar zona\t3-Mostrar\t4-Salir"))
    while (op!=4):
        unMenu.manejador(op)
        op=int (input("Seleecione la opcion deseada\n\t1-Listar Personas\t2-Buscar zona\t3-Mostra\t4-Salir"))
    print ("Adios")

