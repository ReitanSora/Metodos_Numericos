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
from static import style
import functions.events as event


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
        # ventana_login = Login()
        # ventana_login.mainloop()

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
        self.texto_usuario = tk.StringVar()
        tk.Entry(infoFrame,
                 textvariable=self.texto_usuario,
                 **style.STYLE_ENTRY,
                 ).grid(row=0, column=1, pady="20", padx="20")

        # entry apellido
        self.texto_clave = tk.StringVar()
        tk.Entry(infoFrame,
                 textvariable=self.texto_clave,
                 **style.STYLE_ENTRY
                 ).grid(row=1, column=1, pady="20", padx="20")

        # entry nickname
        self.texto_clave = tk.StringVar()
        tk.Entry(infoFrame,
                 textvariable=self.texto_clave,
                 **style.STYLE_ENTRY
                 ).grid(row=2, column=1, pady="20", padx="20")

        # entry correo
        self.texto_clave = tk.StringVar()
        tk.Entry(infoFrame,
                 textvariable=self.texto_clave,
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
