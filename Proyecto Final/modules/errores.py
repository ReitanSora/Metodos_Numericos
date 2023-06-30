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
from tkinter import messagebox
from static import style
import functions.events as event


class Errores(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(background=style.BG)
        self.init_widgets()

    def move(self):
        self.controller.move_to_home()

    def init_widgets(self):
        tk.Label(self,
                 text="Errores",
                 **style.STYLE_TITTLE,
                 ).pack(side=tk.TOP, fill=tk.BOTH, pady=30)

        inputFrame = tk.Frame(self, background=style.BG)
        inputFrame.columnconfigure(0, weight=1)
        inputFrame.pack(side=tk.TOP, fill=tk.BOTH)

        # label ecuacion
        tk.Label(inputFrame,
                 text="Valor expresión 1",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0)

        # label exponente
        tk.Label(inputFrame,
                 text="Valor expresión 2",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=0)

        # label respuesta
        tk.Label(inputFrame,
                 text="Respuesta\necuación 1",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=2, column=0)

        # label respuesta
        tk.Label(inputFrame,
                 text="Respuesta\necuación 2",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=3, column=0)

        # entry valor 1
        self.valor_1 = tk.StringVar()
        tk.Entry(inputFrame,
                 textvariable=self.valor_1,
                 **style.STYLE_ENTRY_SCREENS,
                 ).grid(row=0, column=1, pady=(10, 20), padx="20")

        # entry valor 2
        self.valor_2 = tk.StringVar()
        tk.Entry(inputFrame,
                 textvariable=self.valor_2,
                 **style.STYLE_ENTRY_SCREENS,
                 ).grid(row=1, column=1, pady=(20, 20), padx="20")

        # entry desactivado formula 1
        self.formula_1 = tk.StringVar()
        tk.Entry(inputFrame,
                 textvariable=self.formula_1,
                 **style.STYLE_ENTRY_SCREENS_DES,
                 ).grid(row=0, column=2, pady=(10, 20), padx="20")

        # entry desactivado formula 2
        self.formula_2 = tk.StringVar()
        tk.Entry(inputFrame,
                 textvariable=self.formula_2,
                 **style.STYLE_ENTRY_SCREENS_DES,
                 ).grid(row=1, column=2, pady=(20, 20), padx="20")

        # entry desactivado respuesta
        self.respuesta_1 = tk.StringVar()
        tk.Entry(inputFrame,
                 textvariable=self.respuesta_1,
                 **style.STYLE_ENTRY_SCREENS_DES,
                 ).grid(row=2, column=1, columnspan=2, pady=(50, 20), padx="20", sticky=tk.EW)

        # entry desactivado respuesta
        self.respuesta_2 = tk.StringVar()
        tk.Entry(inputFrame,
                 textvariable=self.respuesta_2,
                 **style.STYLE_ENTRY_SCREENS_DES,
                 ).grid(row=3, column=1, columnspan=2, pady=(20, 20), padx="20", sticky=tk.EW)

        # boton para calcular
        borde_1 = tk.LabelFrame(inputFrame,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.grid(row=0, rowspan=2, column=3, pady="30", padx="20")

        boton_calculo = tk.Button(borde_1,
                                  text="Calcular",
                                  **style.STYLE_BUTTON,
                                  )
        boton_calculo.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_calculo.bind('<Enter>', event.on_enter)
        boton_calculo.bind('<Leave>', event.on_leave)

        # boton para regresar
        borde_2 = tk.LabelFrame(self,
                                **style.STYLE_BUTTON_RETURN_BORDER)
        borde_2.pack(side=tk.BOTTOM, pady=(0, 20))

        boton_return = tk.Button(borde_2,
                                 text="Regresar",
                                 **style.STYLE_BUTTON_RETURN,
                                 command=self.move
                                 )
        boton_return.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_return.bind('<Enter>', event.on_enter_return)
        boton_return.bind('<Leave>', event.on_leave_return)
