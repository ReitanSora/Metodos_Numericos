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
from static import style
import functions.events as event


class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG, pady=50)
        self.controller = controller
        self.init_widgets()

    def init_widgets(self):

        # label titulo bienvenida
        tk.Label(
            self,
            text="Bienvenido al programa de\nMétodos Numéricos",
            # desempaquetado del diccionario STYLE
            **style.STYLE_TITTLE,
        ).pack(side=tk.TOP, fill=tk.X,)