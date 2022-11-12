# Importaciones para conectar a mySql
import mysql.connector
from mysql.connector import Error

# Clase para la conexión a la base de datos, contiene el string de conexión(Conector) y las funciones con los scripts que se van a ejecutar

# DAO: Clase data access objet
# Las funciones se pueden llamar desde una clase


class DAO():

    def __init__(self):
        try:  # El try Except sirve para obtener errores en caso de que sucedan
            self.conexion = mysql.connector.connect(  # String de conexión. Contiene:
                host='localhost',  # Nombre del servidor
                port=3306,  # Numero de puerto
                user='root',  # Nombre del usuario
                password='',  # Contraseña
                db='peluqueria'  # Base de datos
            )
            print("Conexión principal realizada con éxito")
        except Error as ex:
            print("Error al intentar la conexión Principal: {0}".format(ex))

    def listarCitas(self):  # Metodo paara consultar las citas en la base de datos
        if self.conexion.is_connected():
            try:
                # definir una variable que es de tipo self.conexion.cursor() que es un metodo propio de mysql.connector
                cursor = self.conexion.cursor()
                # Con el cursor se ejecuta un script en la base de datos- pide que seleccione todo(*) de(from) cita(tabla) y que lo ordene por Fecha ascendente
                cursor.execute("SELECT * FROM cita ORDER BY Fecha ASC")
                # creamos una variable que es de tipo cursor(Nieto de mysql.connector) y con el fetchall(extraer todo) tomamos los datos que devolvio la consulta anterior
                resultados = cursor.fetchall()
                return resultados  # Retornamos el resultado
            except Error as ex:
                print(
                    "Error al intentar la conexión de la consulta de datos: {0}".format(ex))

    def registrarCita(self, cita): #funcion.
        if self.conexion.is_connected(): #Conexión valida.
            try:
                cursor = self.conexion.cursor() # Propio de mysql.connector
                # Es importante que los elementos de la lista que se esta armando tengan el mismo formato y tipo de dato que en la bd
                sql = "INSERT INTO cita (IdCliente ,Servicio, Cliente, Costo, Fecha, Hora) VALUES ('{0}', '{1}', '{2}', {3}, '{4}','{5}')" #variable dentro de variable(cita) ingresamos datos del cliente.
                cursor.execute(sql.format(  
                    cita[0], cita[1], cita[2], cita[3], cita[4], cita[5])) #se ejecuta el formato de sql(en orden en que ingrese los datos)
                self.conexion.commit() #
                print("Cita registrada!\n") #Muestra la cita registrada
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
