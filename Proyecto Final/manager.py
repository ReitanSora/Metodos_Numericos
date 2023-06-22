'''
Tema: Algoritmos de ordenamiento(iterativos y recursivos)
#Grupo #3
#Integrantes:
#- Stiven Pilca           CI: 1750450262
#- Tulcanza Juan          CI: 1755962485
#Carrera: Ingeniería en Sistemas de la información
#Paralelo: SI4 - 002
#Fecha de entrega: 21/06/2023
'''

import tkinter as tk
from static import style
from screens import Home, Burbuja, Insercion, Seleccion, Shellsort, Mergesort, Quicksort, Heapsort, ShellsortRecursivo


class Manager(tk.Tk):

    def __init__(self, *args, **kwargs):
        # metodo constructor de la clase Tk
        super().__init__(*args, **kwargs)
        self.title("Algoritmos de Ordenamiento")
        self.geometry("800x600")

        # contenedor donde se mostrarán todas las demás ventanas
        container = tk.Frame(self)
        container.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )
        container.configure(background=style.BG)

        # creacion de filas y clumnas disponibles en el frame container,
        # 0 = 1 columna/fila ; weight = espacio que ocupa
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)

        # diccionario de clases
        self.frames = {}

        for F in (Home, Burbuja, Insercion, Seleccion, Shellsort, Mergesort, Quicksort, Heapsort, ShellsortRecursivo):
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
