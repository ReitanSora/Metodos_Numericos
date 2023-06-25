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
from model.usuario import buscar_clave
import functions.events as event


class Login (tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(background=style.BG)
        self.title("Ingreso")
        self.geometry("350x450")
        self.resizable(False, False)
        self.init_widgets()

    def ingresar(self, usuario: str, clave: str):
        clave_registro = buscar_clave(usuario)
        if clave_registro is not None:
            if clave == clave_registro:
                self.destroy()
                Manager()
            else:
                self.texto_alerta.set("Usuario o contraseña mal ingresados")
        else:
            self.texto_alerta.set("Usuario o contraseña mal ingresados")

    def login_event_mouse(self):
        self.ingresar(self.texto_usuario.get(), self.texto_clave.get())

    def login_event_keyboard(self, event):
        self.ingresar(self.texto_usuario.get(), self.texto_clave.get())

    def register_event(self):
        Register()

    def clean(self, event):
        self.texto_alerta.set("")

    def init_widgets(self):
        tk.Label(self,
                 text="Iniciar Sesión",
                 **style.STYLE_TITTLE
                 ).pack(side=tk.TOP, fill=tk.BOTH, pady=20)

        info_frame = tk.Frame(self, background=style.BG)
        info_frame.columnconfigure(0, weight=1)
        info_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True,)

        # label ingreso usuario
        tk.Label(info_frame,
                 text="Ingrese su usuario",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=0, column=0, pady=(10,20))

        # label ingreso clave
        tk.Label(info_frame,
                 text="Ingrese su clave",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=2, column=0, pady=(10,20))

        # label alerta
        self.texto_alerta = tk.StringVar()
        tk.Label(info_frame,
                 textvariable=self.texto_alerta,
                 **style.STYLE_WARNING
                 ).grid(row=4, column=0)

        # ingreso nombre de usuario
        self.texto_usuario = tk.StringVar()
        self.entry_usuario = tk.Entry(info_frame,
                                      textvariable=self.texto_usuario,
                                      **style.STYLE_ENTRY)
        self.entry_usuario.grid(row=1, column=0, pady=(0,20))

        self.entry_usuario.bind("<Return>", self.login_event_keyboard)

        # ingreso clave del usuario
        self.texto_clave = tk.StringVar()
        self.entry_clave = tk.Entry(info_frame,
                                    textvariable=self.texto_clave,
                                    **style.STYLE_ENTRY,
                                    show="*"
                                    )
        self.entry_clave.grid(row=3, column=0, pady=(0,20))

        self.entry_clave.bind("<Return>", self.login_event_keyboard)

        # boton para logearse
        borde_1 = tk.LabelFrame(self,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.pack(side=tk.TOP, expand=True, pady=(0,20))

        boton_login = tk.Button(borde_1,
                                text="Ingresar",
                                **style.STYLE_BUTTON,
                                command=self.login_event_mouse)
        boton_login.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        boton_login.bind('<Enter>', event.on_enter)
        boton_login.bind('<Leave>', event.on_leave)

        # boton para registrarse
        borde_2 = tk.LabelFrame(self,
                                **style.STYLE_BUTTON_BORDER)
        borde_2.pack(side=tk.TOP, expand=True, pady=(0,20))

        boton_registro = tk.Button(borde_2,
                                   text="Registrarse",
                                   **style.STYLE_BUTTON,
                                   command=self.register_event)
        boton_registro.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        boton_registro.bind('<Enter>', event.on_enter)
        boton_registro.bind('<Leave>', event.on_leave)

        self.entry_usuario.bind('<KeyRelease-Return>', self.login_event_keyboard)
        self.entry_clave.bind('<KeyRelease-Return>', self.login_event_keyboard)
        self.entry_usuario.bind('<KeyRelease>', self.clean)
        self.entry_clave.bind('<KeyRelease>', self.clean)