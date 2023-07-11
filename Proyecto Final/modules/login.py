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

import tkinter as tk
import os
import functions.events as event
from modules import manager
from modules import register
from static import style
from model import usuario


class Login (tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(background=style.BG)
        self.title("Ingreso")
        self.geometry("350x450")
        self.resizable(False, False)
        ruta_icono = os.path.abspath("./resources/icon.ico")
        self.iconbitmap(ruta_icono)
        self.init_widgets()

    def ingresar(self, usuario_nick: str, clave: str):
        usuario.crear_tabla()
        clave_registro = usuario.buscar(usuario_nick, 3)

        if clave == clave_registro:
            self.destroy()
            ventana = manager.Manager()
            ventana.mainloop()
        else:
            self.texto_alerta.set("Usuario o contraseña mal ingresados")

    def login_event_mouse(self):
        self.ingresar(self.texto_usuario.get(), self.texto_clave.get())

    def login_event_keyboard(self, event):
        self.ingresar(self.texto_usuario.get(), self.texto_clave.get())

    def register_event(self):
        ventana = register.Register()
        ventana.mainloop()

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
                 ).grid(row=0, column=0, pady=(10, 20))

        # label ingreso clave
        tk.Label(info_frame,
                 text="Ingrese su clave",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=2, column=0, pady=(10, 20))

        # label alerta
        self.texto_alerta = tk.StringVar()
        tk.Label(info_frame,
                 textvariable=self.texto_alerta,
                 **style.STYLE_WARNING
                 ).grid(row=4, column=0)

        # ingreso nombre de usuario
        borde_entry_1 = tk.LabelFrame(info_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_1.grid(row=1, column=0, pady=(0, 20), padx=40)

        self.texto_usuario = tk.StringVar()
        entry_usuario = tk.Entry(borde_entry_1,
                                 textvariable=self.texto_usuario,
                                 **style.STYLE_ENTRY,
                                 )
        entry_usuario.pack()

        entry_usuario.bind("<Return>", self.login_event_keyboard)

        canvas_linea_1 = tk.Canvas(borde_entry_1, **style.STYLE_CANVAS)
        canvas_linea_1.pack(side=tk.TOP, fill=tk.X, anchor=tk.CENTER)
        canvas_linea_1.create_line(
            0, 0, 275, 0, **style.STYLE_CANVAS_LINE)

        # ingreso clave del usuario
        borde_entry_2 = tk.LabelFrame(info_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_2.grid(row=3, column=0, pady=(0, 20), padx=40)

        self.texto_clave = tk.StringVar()
        entry_clave = tk.Entry(borde_entry_2,
                               textvariable=self.texto_clave,
                               **style.STYLE_ENTRY,
                               show="*"
                               )
        entry_clave.pack()

        entry_clave.bind("<Return>", self.login_event_keyboard)

        canvas_linea_2 = tk.Canvas(borde_entry_2, **style.STYLE_CANVAS)
        canvas_linea_2.pack(side=tk.TOP, fill=tk.X, anchor=tk.CENTER)
        canvas_linea_2.create_line(
            0, 0, 275, 0, **style.STYLE_CANVAS_LINE)

        # boton para logearse
        borde_1 = tk.LabelFrame(self,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.pack(side=tk.TOP, expand=True, pady=(0, 20))

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
        borde_2.pack(side=tk.TOP, expand=True, pady=(0, 20))

        boton_registro = tk.Button(borde_2,
                                   text="Registrarse",
                                   **style.STYLE_BUTTON,
                                   command=self.register_event)
        boton_registro.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        boton_registro.bind('<Enter>', event.on_enter)
        boton_registro.bind('<Leave>', event.on_leave)

        entry_usuario.bind('<KeyRelease-Return>',
                           self.login_event_keyboard)
        entry_clave.bind('<KeyRelease-Return>', self.login_event_keyboard)
        entry_usuario.bind('<KeyRelease>', self.clean)
        entry_clave.bind('<KeyRelease>', self.clean)
