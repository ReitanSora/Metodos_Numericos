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
import functions.events as event
from static import style

class Navegacion (tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.controller = parent
        self.init_widgets(parent)

    def init_widgets(self, parent):
        nav_frame = tk.Frame(parent)
        nav_frame.pack(side=tk.LEFT, fill=tk.Y)
        nav_frame.configure(background=style.COLOR_AQUA, borderwidth=0)

        boton_inicio = tk.Button(nav_frame,
                  text="Inicio",
                  **style.STYLE_BUTTON_NAV,
                  command=parent.move_to_home
                  )
        boton_inicio.pack(side= tk.TOP, fill=tk.BOTH, expand=False)

        boton_inicio.bind('<Enter>', event.on_enter_nav)
        boton_inicio.bind('<Leave>', event.on_leave_nav)

        boton_errores = tk.Button(nav_frame,
                  text="Errores",
                  **style.STYLE_BUTTON_NAV,
                  command=parent.move_to_errores
                  )
        boton_errores.pack(side= tk.TOP, fill=tk.BOTH, expand=False)

        boton_errores.bind('<Enter>', event.on_enter_nav)
        boton_errores.bind('<Leave>', event.on_leave_nav)

        boton_numeracion = tk.Button(nav_frame,
                  text="Sistemas de\nnumeración",
                  **style.STYLE_BUTTON_NAV,
                  command=parent.move_to_sistemas
                  )
        boton_numeracion.pack(side= tk.TOP, fill=tk.BOTH, expand=False)

        boton_numeracion.bind('<Enter>', event.on_enter_nav)
        boton_numeracion.bind('<Leave>', event.on_leave_nav)

        boton_flotante = tk.Button(nav_frame,
                  text="Punto Flotante",
                  **style.STYLE_BUTTON_NAV,
                  command=parent.move_to_flotante
                  )
        boton_flotante.pack(side= tk.TOP, fill=tk.BOTH, expand=False)

        boton_flotante.bind('<Enter>', event.on_enter_nav)
        boton_flotante.bind('<Leave>', event.on_leave_nav)

        # boton para navegar al ejercicio de Teorema de Bolzano
        boton_bolzano = tk.Button(nav_frame,
                  text="Teorema de\nBolzano",
                  **style.STYLE_BUTTON_NAV,
                  command=parent.move_to_bolzano
                  )
        boton_bolzano.pack(side= tk.TOP, fill=tk.BOTH, expand=False)

        boton_bolzano.bind('<Enter>', event.on_enter_nav)
        boton_bolzano.bind('<Leave>', event.on_leave_nav)

        # boton para navegar al ejercicio de Metodo de Biseccion
        boton_biseccion = tk.Button(nav_frame,
                  text="Método de\nBisección",
                  **style.STYLE_BUTTON_NAV,
                  command=parent.move_to_biseccion
                  )
        boton_biseccion.pack(side= tk.TOP, fill=tk.BOTH, expand=False)

        boton_biseccion.bind('<Enter>', event.on_enter_nav)
        boton_biseccion.bind('<Leave>', event.on_leave_nav)

        # label de información - footer
        tk.Label(nav_frame,
                text="Proyecto Primer Hemi\nGrupo-6",
                font=("Corbel", 10, "normal"),
                background=style.COLOR_AQUA,
                foreground="#FFF",
                justify="center"
                ).pack(side=tk.BOTTOM, fill=tk.BOTH)
        
    