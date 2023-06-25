from .conection import ConectionDB
import sqlite3


def crear_tabla() -> None:
    conexion = ConectionDB()

    puntero_persona = conexion.cursor_persona()

    sql_personas = '''
    CREATE TABLE personas(
        id_persona INTEGER,
        nombre_persona VARCHAR(50),
        apellido_persona VARCHAR(50),
        correo_persona VARCHAR(50),
        PRIMARY KEY(id_persona AUTOINCREMENT)
    )'''

    try:
        puntero_persona.execute(sql_personas)
        conexion.close()
    except sqlite3.OperationalError:
        pass


def borrar_tabla():
    conexion = ConectionDB()

    puntero = conexion.cursor_persona()

    sql = 'DROP TABLE personas'

    try:
        puntero.execute(sql)
        conexion.close()
    except sqlite3.OperationalError:
        pass


class Persona:
    def __init__(self, nombre_persona, apellido_persona, correo_persona):
        self.id_persona = None
        self.nombre_persona = nombre_persona
        self.apellido_persona = apellido_persona
        self.correo_persona = correo_persona

    def __str__(self):
        return f'Persona[{self.nombre_persona},{self.apellido_persona},{self.correo_persona}]'


def ingresar(objeto: Persona) -> None:
    conexion = ConectionDB()

    puntero_persona = conexion.cursor_persona()

    sql_persona = "INSERT INTO personas(nombre_persona, apellido_persona, correo_persona) VALUES(?,?,?)"

    data_persona = (objeto.nombre_persona,
                    objeto.apellido_persona, objeto.correo_persona)

    puntero_persona.execute(sql_persona, data_persona)
    conexion.close()


def editar(objeto: Persona, id_persona):
    conexion = ConectionDB()

    puntero = conexion.cursor_persona()

    sql = "UPDATE peliculas SET nombre_usuario = ?, clave_usuario = ? WHERE id_usuario = ?"

    datos = (objeto.nombre_usuario, objeto.clave_usuario, objeto.id_usuario)

    puntero.execute(sql, datos)
    conexion.close()


def buscar_correo(correo_persona: str) -> int:
    conexion = ConectionDB()

    puntero = conexion.cursor_persona()

    sql = "SELECT * FROM personas WHERE correo_persona = ?"
    dato = (correo_persona,)

    puntero.execute(sql, dato)
    registro = puntero.fetchone()
    conexion.close()
    try:
        return registro[0]
    except TypeError:
        pass
