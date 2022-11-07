from BD.conexion import DAO
import funciones


def menuPrincipal():
    continuar = True
    while (continuar):
        opcionCorrecta = False
        while (not opcionCorrecta):
            print("==================== MENÚ PRINCIPAL ====================")
            print("1.- Listar citas")
            print("2.- Registrar cita")
            print("3.- Actualizar cita")
            print("4.- Eliminar cita")
            print("5.- Salir")
            print("========================================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 5:
                continuar = False
                print("¡Gracias por usar este sistema!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    dao = DAO()

    if opcion == 1:
        try:
            citas = dao.listarCitas()
            if len(citas) > 0:
                funciones.listarCitas(citas)
            else:
                print("No se encontraron citas...")
        except:
            print("Ocurrió un error...")
    elif opcion == 2:
        # En este campo se realiza la función que solicita los datos que va a contener la lista de citas, para luego utilizarlas en el registro de citas.
        cita = funciones.pedirDatosRegistro()
        try:
            # Se registran las citas
            dao.registrarCita(cita)
            citas = dao.listarCitas()
            if len(citas) > 0:
                funciones.listarCitas(citas)
        except:
            print("Ocurrió un error...")
    elif opcion == 3:

        # Se listan las citas de nuevo, en caso de que devuelva data se procede a actualizar
        citas = dao.listarCitas()
        if len(citas) > 0:
            print(citas)
            cita = funciones.pedirDatosActualizacion(citas)
            print(cita)
            if cita:
                dao.actualizarCurso(cita)
            else:
                print("Id de cita a actualizar no encontrado...\n")
        else:
            print("No se encontraron citas...")

    elif opcion == 4:
        try:
            citas = dao.listarCitas()
            if len(citas) > 0:
                IdEliminar = funciones.pedirDatosEliminacion(citas)
                if not (IdEliminar == ""):
                    dao.eliminarCurso(IdEliminar)
                else:
                    print("Id de cita no encontrado...\n")
            else:
                print("No se encontraron citas...")
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")


menuPrincipal()
