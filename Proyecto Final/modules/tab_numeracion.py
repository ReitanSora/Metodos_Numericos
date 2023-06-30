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
from tkinter import ttk
from static import style
from modules.binario_decimal import BinarioDecimal
from modules.octal_hexa_decimal import OctalHexaDecimal


class MenuTabSistemasNumeracion(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG)
        self.controller = controller

        sistemas_numeracion = ttk.Notebook(self)
        sistemas_numeracion.pack(expand=True, fill=tk.BOTH)

        subventana_1 = BinarioDecimal(self, controller)
        subventana_2 = OctalHexaDecimal(self, controller)

        sistemas_numeracion.add(subventana_1, text="B & D")
        sistemas_numeracion.add(subventana_2, text="O & H & D")
