from Menu import menu
def TryExceptBloque(op):
    try:
        int(op)>10
        return int (op)
    except ValueError:
        print("El valor no es un numero")

if __name__=="__main__":
    unmenu=menu()
    op=input("Seleccione la opcion deseada\n1. Cargar los datos de los Equipos en la clase Manejador de Equipos, a partir de los datos registrados en el archivo.\n2. Crear un contrato para un jugador en un equipo: Se genera un contrato para un jugador en un equipo.\n3. Consultar jugadores Contratados: Ingresar el DNI de un jugador, si está contratado, mostrar el nombre del Equipo en el que fue contratado, y la fecha de finalización de contrato.\n4. Consultar Contratos: Ingresar el identificador de un Equipo y listar los datos de los Jugadores cuyo contrato vence en 6 meses.\n5. Obtener importe de contratos: Para un nombre de equipo leído desde teclado, determinar el importe total de los contratos que posee con los jugadores del equipo.\n5. Guardar Contratos: Generar un nuevo archivo que contenga los siguientes datos de los contratos: DNI del jugador, Nombre del equipo, fecha de inicio, fecha de fin, y el pago mensual.\n6. Salir")
    va=TryExceptBloque(op)
    while va!=6:
        unmenu.operador(va)
        op=input("Seleccione la opcion deseada\n1. Cargar los datos de los Equipos en la clase Manejador de Equipos, a partir de los datos registrados en el archivo.\n2. Crear un contrato para un jugador en un equipo: Se genera un contrato para un jugador en un equipo.\n3. Consultar jugadores Contratados: Ingresar el DNI de un jugador, si está contratado, mostrar el nombre del Equipo en el que fue contratado, y la fecha de finalización de contrato.\n4. Consultar Contratos: Ingresar el identificador de un Equipo y listar los datos de los Jugadores cuyo contrato vence en 6 meses.\n5. Obtener importe de contratos: Para un nombre de equipo leído desde teclado, determinar el importe total de los contratos que posee con los jugadores del equipo.\n5. Guardar Contratos: Generar un nuevo archivo que contenga los siguientes datos de los contratos: DNI del jugador, Nombre del equipo, fecha de inicio, fecha de fin, y el pago mensual.\n6. Salir")
        va=TryExceptBloque(op)
