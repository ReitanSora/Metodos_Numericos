'''
Tema: Métodos Numéricos
#Grupo #
#Integrantes:

•	Kevin Josue Amaguaña Rivadeneira
•	Priscila Veronica Chisag Pillajo
•	Andy RIcardo Galarza Morales
•	Stiven Anthony Pilca Sánchez

#Carrera: Ingeniería en Sistemas de la información
#Paralelo: SI4 - 002
'''

class Usuarios():

    def __init__(self, nombre, apellido, nickname, correo_electronico, clave):
        self.nombre = nombre
        self.apellido = apellido
        self.nickname = nickname
        self.correo_electronico = correo_electronico
        self.clave = clave

    def crear(self, nombre: str, apellido: str, nickname: str, correo_electronico: str, clave: str):

        usuario = Usuarios(nombre, apellido, nickname,
                           correo_electronico, clave)

        usuarios = list()
        usuarios.append(usuario)
        print(usuarios)
