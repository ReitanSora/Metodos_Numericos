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


def on_enter(e):
    e.widget.config(**style.STYLE_BUTTON_ENTER)


def on_leave(e):
    e.widget.config(**style.STYLE_BUTTON)


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
        if usuario == "admin" and clave == "123":
            self.destroy()
            ventana_interfaz = Manager()
            ventana_interfaz.mainloop()
        else:
            messagebox.showerror(
                "Error usuario", "El usuario o la clave son incorrectos")

    def login_event(self):
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


if __name__ == "__main__":
    app = Login()
    app.mainloop()
