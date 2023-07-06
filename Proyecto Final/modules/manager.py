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
from modules.tab_errores import MenuTabErrores
from modules.tab_numeracion import MenuTabSistemasNumeracion
from modules.flotante import PuntoFlotante
from modules.home import Home
from modules.menu import Menu
from modules.bolzano import Bolzano


class Manager(tk.Tk):

    def __init__(self, *args, **kwargs):
        # metodo constructor de la clase Tk
        super().__init__(*args, **kwargs)
        self.title("Métodos Numéricos")
        self.geometry("800x600")

        # contenedor donde se mostrarán todas las demás ventanas
        container = tk.Frame(self)
        container.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )
        container.configure(background=style.BG)

        # cinta de opciones
        Menu(parent=self)

        # creacion de filas y clumnas disponibles en el frame container,
        # 0 = 1 columna/fila ; weight = espacio que ocupa
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)

        # diccionario de clases
        self.frames = {}

        for F in (Home, PuntoFlotante, MenuTabErrores, MenuTabSistemasNumeracion, Bolzano):
            frame = F(container, self)
            self.frames[F] = frame

            # configuracion de filas, columnas y rellenado del frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.show_frame(Home)

    # metodo para mostrar las diferentes ventanas
    def show_frame(self, container):
        frame = self.frames[container]

        # para poner una pantalla encima de la otra
        frame.tkraise()

    def salir(self):
        self.destroy()

    def move_to_home(self):
        self.show_frame(Home)

    def move_to_errores(self):
        self.show_frame(MenuTabErrores)

    def move_to_sistemas(self):
        self.show_frame(MenuTabSistemasNumeracion)

    def move_to_flotante(self):
        self.show_frame(PuntoFlotante)

    def move_to_bolzano(self):
        self.show_frame(Bolzano)
