import sqlite3


class ConectionDB:

    def __init__(self):
        self.base_datos_usuario = "./database/usuarios.db"
        self.base_datos_persona = "./database/personas.db"
        self.conexion_usuario = sqlite3.connect(self.base_datos_usuario)
        self.conexion_persona = sqlite3.connect(self.base_datos_persona)
        self.cursor_usuario = self.conexion_usuario.cursor
        self.cursor_persona = self.conexion_persona.cursor

    def close(self):
        self.conexion_usuario.commit()
        self.conexion_persona.commit()
        self.conexion_usuario.close()
        self.conexion_persona.close()
