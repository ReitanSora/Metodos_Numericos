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
import os

class ConectionDB:

    def __init__(self):
        ruta = os.path.abspath("./database/usuarios.db")
        self.base_datos_usuario = ruta
        self.conexion_usuario = sqlite3.connect(self.base_datos_usuario)
        self.cursor_usuario = self.conexion_usuario.cursor

    def close(self):
        self.conexion_usuario.commit()
        self.conexion_usuario.close()
