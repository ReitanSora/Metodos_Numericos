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
from static import style


def on_enter(e):
    e.widget.config(**style.STYLE_BUTTON_ENTER)


def on_leave(e):
    e.widget.config(**style.STYLE_BUTTON)


class Register(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(background=style.BG)
        self.title("Registro nuevo usuario")
        self.geometry("500x700")
        #self.resizable(False, False)
        self.init_widgets()


    def init_widgets(self):

        
        tk.Label(self, 
                 text="Registro",
                 **style.STYLE_TITTLE
                 ).pack(side=tk.TOP, fill=tk.BOTH, pady="10")

        infoFrame = tk.Frame(self, background=style.BG)
        infoFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True,)

        # ingreso nombre de usuario
        borde_1 = tk.LabelFrame(infoFrame,
                                **style.STYLE_LABEL_FRAME)
        borde_1.grid(row=1,column=0, pady="20", padx="10")

        tk.Label(borde_1, 
                 text="Ingrese su nombre", 
                 **style.STYLE_SUBTITTLE
                 ).pack()

        borde_2 = tk.LabelFrame(infoFrame,
                                **style.STYLE_LABEL_FRAME)
        borde_2.grid(row=1,column=1, pady="20",padx="30")

        self.texto_usuario = tk.StringVar()
        self.entry_usuario = tk.Entry(borde_2,
                                      textvariable=self.texto_usuario,
                                      **style.STYLE_ENTRY)
        self.entry_usuario.pack(side=tk.RIGHT, expand=True)

        # ingreso clave del usuario
        tk.Label(self,
                 text="Ingrese su clave",
                 **style.STYLE_SUBTITTLE).pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=0)

        self.texto_clave = tk.StringVar()
        self.entry_clave = tk.Entry(self,
                                    textvariable=self.texto_clave,
                                    **style.STYLE_ENTRY)
        self.entry_clave.pack(side=tk.RIGHT, expand=True)

        # # boton para logearse
        # borde_1 = tk.LabelFrame(self,
        #                         **style.STYLE_BUTTON_BORDER)
        # borde_1.pack(side=tk.TOP, expand=True)

        # boton_login = tk.Button(borde_1,
        #                         text="Ingresar",
        #                         **style.STYLE_BUTTON,
        #                         )
        # boton_login.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        # boton_login.bind('<Enter>', on_enter)
        # boton_login.bind('<Leave>', on_leave)

        # # boton para registrarse
        # borde_2 = tk.LabelFrame(self,
        #                         **style.STYLE_BUTTON_BORDER)
        # borde_2.pack(side=tk.TOP, expand=True)

        # boton_registro = tk.Button(borde_2,
        #                            text="Registrarse",
        #                            **style.STYLE_BUTTON,
        #                            )
        # boton_registro.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        # boton_registro.bind('<Enter>', on_enter)
        # boton_registro.bind('<Leave>', on_leave)