import sqlite3
import os
from pathlib import Path

class ConectionDB:

    def __init__(self):
        ruta_1 = os.path.join(os.getcwd(), 'database/usuarios.db')
        ruta_2 = os.path.join(os.getcwd(), 'database/personas.db')
        #print(ruta_1)
        #print(type(ruta_1))
        #os.makedirs(os.path.join(ruta, 'prueba'))
        #print(os.path.exists(ruta_1))
        self.base_datos_usuario = ruta_1
        self.base_datos_persona = ruta_2
        self.conexion_usuario = sqlite3.connect(self.base_datos_usuario)
        self.conexion_persona = sqlite3.connect(self.base_datos_persona)
        self.cursor_usuario = self.conexion_usuario.cursor
        self.cursor_persona = self.conexion_persona.cursor

    def close(self):
        self.conexion_usuario.commit()
        self.conexion_persona.commit()
        self.conexion_usuario.close()
        self.conexion_persona.close()
