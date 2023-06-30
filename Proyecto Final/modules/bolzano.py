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
from tkinter import messagebox
from static import style
import functions.events as event


class Bolzano(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(background=style.BG)
        self.init_widgets()

    def move_home(self):
        self.controller.move_to_home()

    def init_widgets(self):
        tk.Label(self,
                 text="Teorema de Bolzano",
                 **style.STYLE_TITTLE,
                 ).pack(side=tk.TOP, fill=tk.BOTH, pady=30)