from datetime import date
import sqlite3

"""
SELECT id, fecha, concepto, tipo, cantidad FROM movimientos
"""


class DBManager:
    """
    Clase para interactuar con la base de datos SQLite
    """

    def __init__(self, ruta):
        self.ruta = ruta  # Ruta de la base de datos SQLite.

    def consultaSQL(self, consulta):
        # Método para ejecutar una consulta SQL y obtener los resultados.
        # 1. Conectar a la base de datos
        conexion = sqlite3.connect(self.ruta)

        # 2. Abrir un cursor
        cursor = conexion.cursor()

        # 3. Ejecutar la consulta SQL sobre ese cursor
        cursor.execute(consulta)

        # 4. Tratar los datos
        # 4.1 obtener los datos
        datos = cursor.fetchall()

        self.movimientos = []
        nombres_columna = []
        for columna in cursor.description:
            nombres_columna.append(columna[0])

        for dato in datos:
            indice = 0
            movimiento = {}
            for nombre in nombres_columna:
                movimiento[nombre] = dato[indice]
                indice += 1

            self.movimientos.append(movimiento)

        # 5. Cerrar la conexión
        conexion.close()

        # 6. Devolver la colección de resultados
        return self.movimientos

    def conectar(self):
        # Método para establecer una conexión a la base de datos.
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()

        return conexion, cursor

    def desconectar(self, conexion):
        # Método para cerrar la conexión a la base de datos.
        conexion.close()

    def consultaConParametros(self, consulta, params):
        # Método para ejecutar una consulta con parámetros y manejar las excepciones.
        conexion, cursor = self.conectar()

        resultado = False
        try:
            cursor.execute(consulta, params)
            conexion.commit()
            resultado = True
        except Exception as ex:
            print(ex)
            conexion.rollback()

        self.desconectar(conexion)
        return resultado

    def borrar(self, id):
        # Método para eliminar un movimiento por su ID de la base de datos.
        consulta = 'DELETE FROM movimientos WHERE id=?'
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        resultado = False
        try:
            cursor.execute(consulta, (id,))
            conexion.commit()
            resultado = True
        except:
            conexion.rollback()

        conexion.close()
        return resultado

    def obtenerMovimiento(self, id):
        # Método para obtener un movimiento por su ID de la base de datos y formatear la fecha.
        """
        Obtiene un movimiento a partir de su ID de la base de datos
        """
        consulta = 'SELECT id, fecha, concepto, tipo, cantidad FROM movimientos WHERE id=?'
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        cursor.execute(consulta, (id,))

        datos = cursor.fetchone()
        resultado = None

        if datos:
            nombres_columna = []
            for column in cursor.description:
                nombres_columna.append(column[0])

            # nombres_columna = ['id', 'fecha', 'concepto', 'tipo', 'cantidad']
            # datos           = ( 3,  2023-02-28, 'Camiseta', 'G',   15.00)
            movimiento = {}
            indice = 0
            for nombre in nombres_columna:
                movimiento[nombre] = datos[indice]
                indice += 1

            print(f'Fecha ANTES: {movimiento["fecha"]}')
            movimiento['fecha'] = date.fromisoformat(movimiento['fecha'])
            print(f'DESPUÉS:     {movimiento["fecha"]}')

            resultado = movimiento

        conexion.close()
        return resultado
