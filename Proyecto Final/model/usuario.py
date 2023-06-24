from .conection import ConectionDB
from tkinter import messagebox
import sqlite3


def crear_tabla():
    conexion = ConectionDB()

    puntero = conexion.cursor()

    sql = '''
    CREATE TABLE usuarios(
        id_usuario INTEGER,
        nombre_usuario VARCHAR(50),
        clave_usuario VARCHAR(10),
        PRIMARY KEY(id_usuario AUTOINCREMENT) 
    )'''
    try:
        puntero.execute(sql)
        conexion.close()

    except sqlite3.OperationalError:
        pass


def borrar_tabla():
    conexion = ConectionDB()

    puntero = conexion.cursor()

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


def ingresar(objeto: Usuario):
    conexion = ConectionDB()

    puntero = conexion.cursor()

    sql = "INSERT INTO usuarios(nombre_usuario, clave_usuario) VALUES(?,?)"

    data = (objeto.nombre_usuario, objeto.clave_usuario)

    puntero.execute(sql, data)
    conexion.close()


def editar(objeto: Usuario, id_usuario):
    conexion = ConectionDB()

    puntero = conexion.cursor()

    sql = "UPDATE peliculas SET nombre_usuario = ?, clave_usuario = ? WHERE id_usuario = ?"

    datos = (objeto.nombre_usuario, objeto.clave_usuario, objeto.id_usuario)

    puntero.execute(sql, datos)
    conexion.close()


def buscar(nombre_usuario: str):
    conexion = ConectionDB()

    puntero = conexion.cursor()

    sql = "SELECT * FROM usuarios WHERE nombre_usuario = ?"
    dato = (nombre_usuario,)

    puntero.execute(sql, dato)
    registro = puntero.fetchone()
    conexion.close()
    try:
        return registro[2]
    except TypeError:
        pass
