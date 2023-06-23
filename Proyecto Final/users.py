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
import json

usuarios = list()


class Usuarios():

    def __init__(self, nombre, apellido, nickname, correo, clave):
        self.nombre = nombre
        self.apellido = apellido
        self.nickname = nickname
        self.correo = correo
        self.clave = clave


def crear(nombre: str, apellido: str, nickname: str, correo: str, clave: str):

    usuario = Usuarios(nombre, apellido, nickname,
                       correo, clave)

    usuarios.append({
        "nombre": usuario.nombre,
        "apellido": usuario.apellido,
        "nickname": usuario.nickname,
        "correo": usuario.correo,
        "clave": usuario.clave,
    })

    return usuarios


def grabar():
    print(usuarios)
    with open('./test/usuarios.json', 'a') as file:
        json.dump(usuarios, file, indent=4)


def cargar():
    global usuarios

    with open('./test/usuarios.json') as file:
        usuarios = json.load(file)

    for nick in usuarios:
        print(nick.get("nickname"))

    return usuarios

