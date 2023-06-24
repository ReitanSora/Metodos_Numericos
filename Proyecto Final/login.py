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
from register import Register
from static import style
from model.usuario import buscar
import functions.events as event


class Login (tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(background=style.BG)
        self.title("Ingreso")
        self.geometry("350x500")
        self.resizable(False, False)
        # self.tittle("Ventana de prueba")
        # self.geometry("800x600")
        self.init_widgets()

    def ingresar(self, usuario: str, clave: str):
        clave_registro = buscar(usuario)

        if clave_registro != None:
            if clave == clave_registro:
                self.destroy()
                Manager()
            else:
                messagebox.showinfo(
                    "No se encuentra el Usuario", "Usuario o contraseña mal ingresados")

    def login_event_mouse(self):
        self.ingresar(self.texto_usuario.get(), self.texto_clave.get())

    def login_event_keyboard(self, event):
        self.ingresar(self.texto_usuario.get(), self.texto_clave.get())

    def register_event(self):
        Register()

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

        self.entry_usuario.bind("<Return>", self.login_event_keyboard)

        # ingreso clave del usuario
        tk.Label(self,
                 text="Ingrese su clave",
                 **style.STYLE_SUBTITTLE).pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        self.texto_clave = tk.StringVar()
        self.entry_clave = tk.Entry(self,
                                    textvariable=self.texto_clave,
                                    **style.STYLE_ENTRY)
        self.entry_clave.pack(side=tk.TOP, expand=True)

        self.entry_clave.bind("<Return>", self.login_event_keyboard)

        # boton para logearse
        borde_1 = tk.LabelFrame(self,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.pack(side=tk.TOP, expand=True)

        boton_login = tk.Button(borde_1,
                                text="Ingresar",
                                **style.STYLE_BUTTON,
                                command=self.login_event_mouse)
        boton_login.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_login.bind('<Enter>', event.on_enter)
        boton_login.bind('<Leave>', event.on_leave)

        # boton para registrarse
        borde_2 = tk.LabelFrame(self,
                                **style.STYLE_BUTTON_BORDER)
        borde_2.pack(side=tk.TOP, expand=True)

        boton_registro = tk.Button(borde_2,
                                   text="Registrarse",
                                   **style.STYLE_BUTTON,
                                   command=self.register_event)
        boton_registro.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_registro.bind('<Enter>', event.on_enter)
        boton_registro.bind('<Leave>', event.on_leave)
