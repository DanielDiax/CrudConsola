# Importaciones para conectar a mySql
import mysql.connector
from mysql.connector import Error

# Clase para la conexión a la base de datos, contiene el string de conexión(Conector) y las funciones con los scripts que se van a ejecutar


class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='peluqueria'
            )
            print("Conexión principal realizada con éxito")
        except Error as ex:
            print("Error al intentar la conexión Principal: {0}".format(ex))

    def listarCitas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM cita ORDER BY Fecha ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print(
                    "Error al intentar la conexión de la consulta de datos: {0}".format(ex))

    def registrarCita(self, cita):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                # Es importante que los elementos de la lista que se esta armando tengan el mismo formato y tipo de dato que en la bd
                sql = "INSERT INTO cita (IdCliente ,Servicio, Cliente, Costo, Fecha, Hora) VALUES ('{0}', '{1}', '{2}', {3}, '{4}','{5}')"
                cursor.execute(sql.format(
                    cita[0], cita[1], cita[2], cita[3], cita[4], cita[5]))
                self.conexion.commit()
                print("Cita registrada!\n")
            except Error as ex:
                print(
                    "Error al intentar la conexión de la creación de citas: {0}".format(ex))

    def actualizarCita(self, cita):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                #print("Fecha"+'{1}', "Hora" + '{2}', "IdCliente"+'{0}')
                sql = "UPDATE cita SET Fecha = '{0}', Hora = '{1}' WHERE IdCliente = '{2}'"
                cursor.execute(sql.format(cita[1], cita[2], cita[0]))
                self.conexion.commit()
                print("Cita modificada!\n")
            except Error as ex:
                print(
                    "Error al intentar la conexión de la modificación de cita: {0}".format(ex))

    def eliminarCita(self, IdClienteEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM cita WHERE IdCliente = '{0}'"
                cursor.execute(sql.format(IdClienteEliminar))
                self.conexion.commit()
                print("Cita eliminada!\n")
            except Error as ex:
                print(
                    "Error al intentar la conexión de la eliminación: {0}".format(ex))
