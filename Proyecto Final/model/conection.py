import sqlite3


class ConectionDB:

    def __init__(self):
        self.base_datos = "database/usuarios.db"
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor

    def close(self):
        self.conexion.commit()
        self.conexion.close()
