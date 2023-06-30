'''
Tema: Métodos Numéricos
#Grupo #
#Integrantes:

•	Kevin Josue Amaguaña Rivadeneira
•	Priscila Veronica Chisag Pillajo
•	Andy Ricardo Galarza Morales
•	Stiven Anthony Pilca Sánchez

#Carrera: Ingeniería en Sistemas de la información
#Paralelo: SI4 - 002
'''

import tkinter as tk
from static import style
import functions.events as event


class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG, pady=50)
        self.controller = controller
        self.init_widgets()

    def move_to_errores(self):
        self.controller.move_to_errores()

    def move_to_sistemas(self):
        self.controller.move_to_sistemas()

    def move_to_flotante(self):
        self.controller.move_to_flotante()

    def move_to_bolzano(self):
        self.controller.move_to_bolzano()

    def init_widgets(self):

        # label titulo bienvenida
        tk.Label(
            self,
            text="Bienvenido al programa de\nMétodos Numéricos",
            # desempaquetado del diccionario STYLE
            **style.STYLE_TITTLE,
        ).pack(side=tk.TOP, fill=tk.BOTH, pady=0)

        optionsFrame = tk.Frame(self, background=style.BG)
        optionsFrame.columnconfigure(0, weight=1)
        optionsFrame.columnconfigure(1, weight=1)
        optionsFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady="30")

        # Primer boton
        borde_1 = tk.LabelFrame(optionsFrame, **style.STYLE_BUTTON_BORDER)
        borde_1.grid(row=0, column=0, pady="20")

        boton_1 = tk.Button(
            borde_1,
            text="Errores",
            command=self.move_to_errores,
            ** style.STYLE_BUTTON,
        )
        boton_1.pack(expand=True, fill=tk.BOTH)

        boton_1.bind('<Enter>', event.on_enter)
        boton_1.bind('<Leave>', event.on_leave)

        # Segundo boton
        borde_2 = tk.LabelFrame(optionsFrame, **style.STYLE_BUTTON_BORDER)
        borde_2.grid(row=0, column=1, pady="20")

        boton_2 = tk.Button(
            borde_2,
            text="Sistemas de\nNumeración",
            command=self.move_to_sistemas,
            ** style.STYLE_BUTTON,
        )
        boton_2.pack(expand=True, fill=tk.BOTH)

        boton_2.bind('<Enter>', event.on_enter)
        boton_2.bind('<Leave>', event.on_leave)

        # Tercer boton

        borde_3 = tk.LabelFrame(optionsFrame, **style.STYLE_BUTTON_BORDER)
        borde_3.grid(row=1, column=0, pady="20")

        boton_3 = tk.Button(
            borde_3,
            text="Punto\nFlotante",
            command=self.move_to_flotante,
            ** style.STYLE_BUTTON,
        )
        boton_3.pack(expand=True, fill=tk.BOTH)

        boton_3.bind('<Enter>', event.on_enter)
        boton_3.bind('<Leave>', event.on_leave)

        # Cuanto boton
        borde_4 = tk.LabelFrame(optionsFrame, **style.STYLE_BUTTON_BORDER)
        borde_4.grid(row=1, column=1, pady="20")

        boton_4 = tk.Button(
            borde_4,
            text="Teorema de\nBolzano",
            command=self.move_to_bolzano,
            ** style.STYLE_BUTTON,
        )
        boton_4.pack(expand=True, fill=tk.BOTH)

        boton_4.bind('<Enter>', event.on_enter)
        boton_4.bind('<Leave>', event.on_leave)

        # Quinta opcion
        borde_5 = tk.LabelFrame(optionsFrame, **style.STYLE_BUTTON_BORDER)
        borde_5.grid(row=2, column=0, pady="20")

        boton_5 = tk.Button(
            borde_5,
            text="Teorema de\nBisección",
            ** style.STYLE_BUTTON,
        )
        boton_5.pack(expand=True, fill=tk.BOTH)

        boton_5.bind('<Enter>', event.on_enter)
        boton_5.bind('<Leave>', event.on_leave)
