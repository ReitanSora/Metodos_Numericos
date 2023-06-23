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

import tkinter as tk
from tkinter import messagebox
from manager import Manager
from static import style
from users import crear, grabar, cargar, usuarios
import functions.events as event


def on_enter(e):
    e.widget.config(**style.STYLE_BUTTON_ENTER)


def on_leave(e):
    e.widget.config(**style.STYLE_BUTTON)


class Login (tk.Tk):
    lista_usuarios = dict()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(background=style.BG)
        self.title("Ingreso")
        self.geometry("350x500")
        self.resizable(False, False)
        # self.tittle("Ventana de prueba")
        # self.geometry("800x600")
        self.init_widgets()

    def buscar (self, usuario: str):
        self.lista_usuarios = cargar()
        print(self.lista_usuarios)
        if usuario in self.lista_usuarios.values():
            print("Encontrado")
        posicion = self.lista_usuarios.index(usuario)
        print(self.lista_usuarios[posicion])


    def ingresar(self, usuario: str, clave: str):
        if usuario == "admin" and clave == "123":
            self.destroy()
            ventana_interfaz = Manager()
            ventana_interfaz.mainloop()
        else:
            messagebox.showerror(
                "Error usuario", "El usuario o la clave son incorrectos")

    def login_event(self):
        #self.buscar(self.texto_usuario.get())
        self.ingresar(self.texto_usuario.get(), self.texto_clave.get())

    def register_event(self):
        self.destroy()
        ventana_registro = Register()
        ventana_registro.mainloop()

    def init_widgets(self):
        tk.Label(self, text="Iniciar Sesión",
                 **style.STYLE_TITTLE).pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        # ingreso nombre de usuario
        tk.Label(self, text="Ingrese su usuario", **
                 style.STYLE_SUBTITTLE).pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        self.texto_usuario = tk.StringVar()
        self.entry_usuario = tk.Entry(self,
                                      textvariable=self.texto_usuario,
                                      **style.STYLE_ENTRY)
        self.entry_usuario.pack(side=tk.TOP, expand=True)

        # ingreso clave del usuario
        tk.Label(self,
                 text="Ingrese su clave",
                 **style.STYLE_SUBTITTLE).pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        self.texto_clave = tk.StringVar()
        self.entry_clave = tk.Entry(self,
                                    textvariable=self.texto_clave,
                                    **style.STYLE_ENTRY)
        self.entry_clave.pack(side=tk.TOP, expand=True)

        # boton para logearse
        borde_1 = tk.LabelFrame(self,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.pack(side=tk.TOP, expand=True)

        boton_login = tk.Button(borde_1,
                                text="Ingresar",
                                **style.STYLE_BUTTON,
                                command=self.login_event)
        boton_login.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_login.bind('<Enter>', on_enter)
        boton_login.bind('<Leave>', on_leave)

        # boton para registrarse
        borde_2 = tk.LabelFrame(self,
                                **style.STYLE_BUTTON_BORDER)
        borde_2.pack(side=tk.TOP, expand=True)

        boton_registro = tk.Button(borde_2,
                                   text="Registrarse",
                                   **style.STYLE_BUTTON,
                                   command=self.register_event)
        boton_registro.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_registro.bind('<Enter>', on_enter)
        boton_registro.bind('<Leave>', on_leave)


class Register(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(background=style.BG)
        self.title("Registro nuevo usuario")
        self.geometry("500x600")
        # self.resizable(False, False)
        self.init_widgets()

    def move_to_login(self):
        self.destroy()
        ventana_login = Login()
        ventana_login.mainloop()

    def registrar_usuario(self):
        crear(self.texto_nombre.get(), self.texto_apellido.get(),
              self.texto_nickname.get(), self.texto_correo.get(), self.texto_clave.get())
        grabar()

    def init_widgets(self):

        # titulo del frame
        tk.Label(self,
                 text="Registro",
                 **style.STYLE_TITTLE
                 ).pack(side=tk.TOP, fill=tk.BOTH, pady="10")

        infoFrame = tk.Frame(self, background=style.BG)
        infoFrame.columnconfigure(0, weight=1)
        infoFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True,)

        # label nombre de usuario
        tk.Label(infoFrame,
                 text="Nombre",
                 **style.STYLE_SUBTITTLE,
                 justify="center"
                 ).grid(row=0, column=0)

        # label apellido del usuario
        tk.Label(infoFrame,
                 text="Apellido",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=1, column=0)

        # label nickname
        tk.Label(infoFrame,
                 text="Nickname",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=2, column=0)

        # label correo electrocnico
        tk.Label(infoFrame,
                 text="Correo",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=3, column=0)

        # label clave
        tk.Label(infoFrame,
                 text="Clave",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=4, column=0)

        # entry nombre usuario
        self.texto_nombre = tk.StringVar()
        tk.Entry(infoFrame,
                 textvariable=self.texto_nombre,
                 **style.STYLE_ENTRY,
                 ).grid(row=0, column=1, pady="20", padx="20")

        # entry apellido
        self.texto_apellido = tk.StringVar()
        tk.Entry(infoFrame,
                 textvariable=self.texto_apellido,
                 **style.STYLE_ENTRY
                 ).grid(row=1, column=1, pady="20", padx="20")

        # entry nickname
        self.texto_nickname = tk.StringVar()
        tk.Entry(infoFrame,
                 textvariable=self.texto_nickname,
                 **style.STYLE_ENTRY
                 ).grid(row=2, column=1, pady="20", padx="20")

        # entry correo
        self.texto_correo = tk.StringVar()
        tk.Entry(infoFrame,
                 textvariable=self.texto_correo,
                 **style.STYLE_ENTRY
                 ).grid(row=3, column=1, pady="20", padx="20")

        # entry clave
        self.texto_clave = tk.StringVar()
        tk.Entry(infoFrame,
                 textvariable=self.texto_clave,
                 **style.STYLE_ENTRY
                 ).grid(row=4, column=1, pady="20", padx="20")

        # boton para registrarse
        borde_1 = tk.LabelFrame(infoFrame,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.grid(row=5, column=0, pady="30")

        boton_register = tk.Button(borde_1,
                                   text="Registrar",
                                   **style.STYLE_BUTTON,
                                   command=self.registrar_usuario
                                   )
        boton_register.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_register.bind('<Enter>', event.on_enter)
        boton_register.bind('<Leave>', event.on_leave)

        # boton para regresar
        borde_2 = tk.LabelFrame(infoFrame,
                                **style.STYLE_BUTTON_RETURN_BORDER)
        borde_2.grid(row=5, column=1, pady="30")

        boton_registro = tk.Button(borde_2,
                                   text="Regresar",
                                   **style.STYLE_BUTTON_RETURN,
                                   command=self.move_to_login
                                   )
        boton_registro.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_registro.bind('<Enter>', event.on_enter_return)
        boton_registro.bind('<Leave>', event.on_leave_return)
