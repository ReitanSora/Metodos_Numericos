'''
Tema: Métodos Numéricos
Grupo 6
Integrantes:

•	Kevin Josue Amaguaña Rivadeneira
•	Priscila Veronica Chisag Pillajo
•	Andy Ricardo Galarza Morales
•	Stiven Anthony Pilca Sánchez

Carrera: Ingeniería en Sistemas de la información
Paralelo: SI4 - 002
'''

import sqlite3
from .conection import ConectionDB

def crear_tabla() -> None:
    conexion = ConectionDB()

    puntero = conexion.cursor_usuario()

    sql = '''
    CREATE TABLE usuarios(
        ID_USUARIO INTEGER,
        NOMBRE_USUARIO VARCHAR(50),
        APELLIDO_USUARIO VARCHAR(50),
        NICKNAME_USUARIO VARCHAR(50),
        CORREO_USUARIO VARCHAR(50),
        CLAVE_USUARIO VARCHAR(25),

        PRIMARY KEY(ID_USUARIO AUTOINCREMENT) 
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
    def __init__(self, nombre_usuario, apellido_usuario, nickname_usuario, correo_usuario, clave_usuario):
        self.id_usuario = None
        self.nombre_usuario = nombre_usuario
        self.apellido_usuario= apellido_usuario
        self.nickname_usuario = nickname_usuario
        self.correo_usuario = correo_usuario
        self.clave_usuario = clave_usuario

    def __str__(self):
        return f'Usuario[{self.nombre_usuario},{self.apellido_usuario},{self.nickname_usuario},{self.correo_usuario},{self.clave_usuario}]'


def ingresar(objeto: Usuario) -> None:
    conexion = ConectionDB()

    puntero = conexion.cursor_usuario()

    sql = "INSERT INTO usuarios(NOMBRE_USUARIO, APELLIDO_USUARIO, NICKNAME_USUARIO, CORREO_USUARIO, CLAVE_USUARIO) VALUES(?,?,?,?,?)"

    data = (objeto.nombre_usuario, objeto.apellido_usuario, objeto.nickname_usuario, objeto.correo_usuario, objeto.clave_usuario)

    puntero.execute(sql, data)
    conexion.close()


def editar(objeto: Usuario, id_usuario):
    conexion = ConectionDB()

    puntero = conexion.cursor_usuario()

    sql = "UPDATE usuarios SET NOMBRE_USUARIO = ?, APELLIDO_USUARIO = ?, NICKNAME_USUARIO = ?, CORREO_USUARIO = ? WHERE ID_USUARIO = ?"

    data = (objeto.nombre_usuario, objeto.apellido_usuario, objeto.nickname_usuario, objeto.correo_usuario, id_usuario)

    puntero.execute(sql, data)
    conexion.close()


def buscar(dato_usuario: str, opcion: int):
    conexion = ConectionDB()

    puntero = conexion.cursor_usuario()
    
    #buscar la posicion del nickname ingresado
    if opcion == 1:
        sql = "SELECT * FROM usuarios WHERE NICKNAME_USUARIO = ?"
        dato = (dato_usuario,)
        try:
            puntero.execute(sql, dato)
            registro = puntero.fetchone()
            conexion.close()
            return registro[0]
        except (sqlite3.OperationalError, TypeError):
            pass
    #buscar la posicion del correo ingresado
    elif opcion == 2:
        sql = "SELECT * FROM usuarios WHERE CORREO_USUARIO = ?"
        dato = (dato_usuario,)
        try:
            puntero.execute(sql, dato)
            registro = puntero.fetchone()
            conexion.close()
            return registro[0]
        except (sqlite3.OperationalError, TypeError):
            pass
    #buscar la clave del nickname ingresado
    elif opcion == 3:
        sql = "SELECT * FROM usuarios WHERE NICKNAME_USUARIO = ?"
        dato = (dato_usuario,)
        try:
            puntero.execute(sql, dato)
            registro = puntero.fetchone()
            conexion.close()
            return registro[5]
        except (sqlite3.OperationalError, TypeError):
            pass
