from .conection import ConectionDB
import sqlite3


def crear_tabla() -> None:
    conexion = ConectionDB()

    puntero = conexion.cursor_usuario()

    sql = '''
    CREATE TABLE usuarios(
        id_usuario INTEGER,
        nombre_usuario VARCHAR(50),
        clave_usuario VARCHAR(10),
        PRIMARY KEY(id_usuario AUTOINCREMENT) 
        )
        '''
    try:
        puntero.execute(sql)
        conexion.close()

    except sqlite3.OperationalError:
        pass


def borrar_tabla():
    conexion = ConectionDB()

    puntero = conexion.cursor_usuario()

    sql = 'DROP TABLE usuarios'

    try:
        puntero.execute(sql)
        conexion.close()
    except sqlite3.OperationalError:
        pass


class Usuario:
    def __init__(self, nombre_usuario, clave_usuario):
        self.id_usuario = None
        self.nombre_usuario = nombre_usuario
        self.clave_usuario = clave_usuario

    def __str__(self):
        return f'Usuario[{self.nombre_usuario},{self.clave_usuario}]'


def ingresar(objeto: Usuario) -> None:
    conexion = ConectionDB()

    puntero = conexion.cursor_usuario()

    sql = "INSERT INTO usuarios(nombre_usuario, clave_usuario) VALUES(?,?)"

    data = (objeto.nombre_usuario, objeto.clave_usuario)

    puntero.execute(sql, data)
    conexion.close()


def editar(objeto: Usuario, id_usuario):
    conexion = ConectionDB()

    puntero = conexion.cursor_usuario()

    sql = "UPDATE peliculas SET nombre_usuario = ?, clave_usuario = ? WHERE id_usuario = ?"

    datos = (objeto.nombre_usuario, objeto.clave_usuario, objeto.id_usuario)

    puntero.execute(sql, datos)
    conexion.close()


def buscar_clave(nombre_usuario: str) -> str:
    conexion = ConectionDB()

    puntero = conexion.cursor_usuario()

    sql = "SELECT * FROM usuarios WHERE nombre_usuario = ?"
    dato = (nombre_usuario,)

    puntero.execute(sql, dato)
    registro = puntero.fetchone()
    conexion.close()
    try:
        return registro[2]
    except TypeError:
        pass


def buscar_nickname(nombre_usuario: str) -> int:
    conexion = ConectionDB()
    puntero = conexion.cursor_usuario()

    sql = "SELECT * FROM usuarios WHERE nombre_usuario = ?"
    dato = (nombre_usuario,)

    puntero.execute(sql, dato)
    registro = puntero.fetchone()
    conexion.close()
    try:
        return registro[0]
    except TypeError:
        pass
