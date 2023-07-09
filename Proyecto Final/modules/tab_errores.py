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
from modules.errores import Errores
from modules.propagacion_error import PropErrores

class MenuTabErrores (tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG)
        self.controller = controller

        estilo = ttk.Style()
        estilo.theme_use('default')
        estilo.layout("TNotebook", [])
        estilo.configure("TNotebook", tabmargins= 0, background= style.BG_OSCURO)
        estilo.configure("TNotebook.Tab", background= style.BG_OSCURO, font=("Corbel", 12, "bold"), foreground = style.COLOR_BLANCO, expand= True, borderwidth= 0, bordercolor= style.BG_OSCURO)
        estilo.map("TNotebook.Tab", background= [("selected", style.COLOR_MAGENTA_CLARO)])

        errores = ttk.Notebook(self)
        errores.pack(expand=True, fill=tk.BOTH)

        subventana_1 = Errores(self, controller)
        subventana_2 = PropErrores(self, controller)

        errores.add(subventana_1, text="Errores")
        errores.add(subventana_2, text="Propagación")
        