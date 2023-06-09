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
import webbrowser
import os
# import pyscreenshot
# from tkinter import filedialog
from tkinter import simpledialog
from static import style
from model import usuario
from modules.tab_errores import MenuTabErrores
from modules.sistemas import Conversiones
from modules.flotante import PuntoFlotante
from modules.home import Home
from modules.menu import Menu
from modules.navegacion import Navegacion
from modules.bolzano import Bolzano
from modules.biseccion import Biseccion


class Manager(tk.Tk):

    def __init__(self, *args, **kwargs):
        # metodo constructor de la clase Tk
        super().__init__(*args, **kwargs)
        self.title("Métodos Numéricos")
        self.geometry("1000x600")
        self.resizable(False, False)

        ruta_icono = os.path.abspath("./resources/icon.ico")
        self.iconbitmap(ruta_icono)

        # contenedor para los botones de navegacion
        Navegacion(self)

        # contenedor donde se mostrarán todas las demás ventanas
        container = tk.Frame(self)
        container.pack(
            side=tk.RIGHT,
            fill=tk.BOTH,
            expand=True
        )
        container.configure(background=style.BG, bd=0)
        container.config(width="800")

        # cinta de opciones
        Menu(parent=self)

        # creacion de filas y clumnas disponibles en el frame container,
        # 0 = 1 columna/fila ; weight = espacio que ocupa
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)

        # diccionario de clases
        self.frames = {}

        for F in (Home, PuntoFlotante, MenuTabErrores, Conversiones, Bolzano, Biseccion):
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
        self.show_frame(Conversiones)

    def move_to_flotante(self):
        self.show_frame(PuntoFlotante)

    def move_to_bolzano(self):
        self.show_frame(Bolzano)

    def move_to_biseccion(self):
        self.show_frame(Biseccion)

    # def screenshot(self):
    #     ruta = os.path.abspath("./")
    #     screenshot = pyscreenshot.grab(
    #         bbox=(self.winfo_rootx(), self.winfo_rooty(), self.winfo_rootx()+1000, self.winfo_rooty()+580))
    #     try:
    #         archivo = filedialog.asksaveasfilename(
    #             title="Guardar captura de pantalla", initialdir=ruta, filetypes=[('Imágen png', '*.png'), ('Imágen jpg', '*.jpg')], defaultextension='.png', )
    #         screenshot.save(archivo)
    #     except ValueError:
    #         pass

    def new_window(self):
        Manager()

    def github(self):
        webbrowser.open('https://github.com/ReitanSora/Metodos_Numericos.git')

    # def eliminar_usuario(self):
    #     nickname = simpledialog.askstring(
    #         title="Eliminación de cuenta", prompt="Ingrese su nombre de usuario")
    #     posicion = usuario.buscar(nickname, 1)
    #     if posicion is not None:
    #         usuario.eliminar(posicion)
    #     else:
    #         pass
