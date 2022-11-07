from datetime import datetime
# Funcion para recibir la lista con las citas, y ordenarla en una nueva lista con un formato determinado en separaciones por pipes


def listarCitas(citas):
    print("\Citas: \n")
    for cita in citas:
        datos = "Id Cliente: {0} | Servicio: {1} | Cliente: {2} |  Costo: {3} | Fecha: {4} | Hora: {5}"
        print(datos.format(cita[0],
              cita[1], cita[2], cita[3], cita[4], cita[5]))
    print(" ")
# ------------------------------------------------------------------------------------------------------
# Funcion para guardar nuevas citas, tiene validaciones para manejar mas facil los datos que van a la bd


def pedirDatosRegistro():
    # Se valida la información que habra en el servicio.
    IdClienteCorrecto = False
    while (not IdClienteCorrecto):
        idCliente = input("Ingrese código: ")
        if len(idCliente) == 6:
            IdClienteCorrecto = True
        else:
            print("Código incorrecto: Debe tener 6 dígitos.")

    opcionCorrecta = False
    while (not opcionCorrecta):

        print("==================== MENÚ SERVICIOS ====================")
        print("1.- Corte de cabello")
        print("2.- Arreglo de uñas")
        print("3.- Spa Facial")
        print("4.- Salir")
        print("========================================================")
        opc = int(input("Seleccione una opción: "))
        if opc < 1 or opc > 4:
            print("Opción incorrecta, ingrese nuevamente...")
        elif opc == 5:
            print("¡Gracias por usar este sistema!")
            break
        else:
            opcionCorrecta = True
            if opc == 1:
                servicio = "Corte de cabello"
            elif opc == 2:
                servicio = "Arreglo de uñas"
            elif opc == 3:
                servicio = "Spa Facial"
    # Hasta aca viene la selección del servicio

    cliente = input("Ingrese nombre del cliente: ")
    # Se obtiene y valida el costo.
    costoCorrecto = False
    while (not costoCorrecto):
        costo = input("Ingrese Costo: ")
        if costo.isnumeric():
            if (int(costo) > 0):
                costoCorrecto = True
                costo = int(costo)
            else:
                print("El costo debe ser mayor a 0.")
        else:
            print("Costo incorrecto: Debe ser un número únicamente.")

    # En esta ocación la fecha y la hora se van a manejar en formato de texto (string)
    fecha = input("Ingrese fecha sin hora de la cita: ")
    Hora = input("Ingrese Hora de la cita: ")

    cita = (idCliente, servicio, cliente, costo, fecha, Hora)
    return cita
# ----------------------------------------------------------------------------------------------------------------------------------------------

# En este controlador se valida que si hayan datos para modificar y de haberlos se valida la informacion que se envia, de lo contrario no envía nada


def pedirDatosActualizacion(citas):
    listarCitas(citas)
    existeCliente = False
    idCliente = input("Ingrese el código del curso a editar: ")
    for cit in citas:
        if cit[0] == idCliente:
            existeCliente = True
            break

    if existeCliente:
        fecha = input("Ingrese fecha a modificar: ")
        hora = input("Ingrese hora a modificar: ")

        cita = (idCliente, fecha, hora)
    else:
        cita = None

    return cita


def pedirDatosEliminacion(citas):
    listarCitas(citas)
    existeCliente = False
    clienteEliminar = input("Ingrese el Id del cliente a eliminar: ")
    for cit in citas:
        if cit[0] == clienteEliminar:
            existeCliente = True
            break

    if not existeCliente:
        clienteEliminar = ""

    return clienteEliminar
