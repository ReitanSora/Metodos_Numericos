class Usuarios():

    def __init__(self, nombre, apellido, nombre_usuario, correo_electronico, clave):
        self.nombre = nombre
        self.apellido = apellido
        self.nombre_usuario = nombre_usuario
        self.correo_electronico = correo_electronico
        self.clave = clave

    def crear (self, nombre: str, apellido: str, nombre_usuario: str, correo_electronico: str, clave: str):

        usuario = Usuarios(nombre, apellido, nombre_usuario, correo_electronico, clave)

        usuarios = list()
        usuarios.append(usuario)
        print(usuarios)


