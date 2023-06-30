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
from tkinter import messagebox
from static import style
import functions.events as event


class PuntoFlotante(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG)
        self.controller = controller
        self.init_widgets()

    def move_to_home(self):
        self.controller.move_to_home()

    def init_widgets(self):
        tk.Label(self,
                 text="Punto Flotante",
                 **style.STYLE_TITTLE,
                 ).pack(side=tk.TOP, fill=tk.BOTH, pady=30)

        inputFrame = tk.Frame(self, background=style.BG)
        inputFrame.columnconfigure(0, weight=1)
        inputFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True,)

        # label numero decimal
        tk.Label(inputFrame,
                 text="Número decimal",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0)

        # label numero decimal con exponente
        tk.Label(inputFrame,
                 text="Número decimal\ncon exponente",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=0)

        # entry numero decimal normal
        self.decimal_normal = tk.StringVar()
        tk.Entry(inputFrame,
                 textvariable=self.decimal_normal,
                 **style.STYLE_ENTRY,
                 ).grid(row=0, column=1, pady="20", padx="20")

        # entry numero decimal con exponente
        self.decimal_exponente = tk.StringVar()
        tk.Entry(inputFrame,
                 textvariable=self.decimal_exponente,
                 **style.STYLE_ENTRY,
                 ).grid(row=1, column=1, pady="20", padx="20")

        # boton para calcular
        borde_1 = tk.LabelFrame(inputFrame,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.grid(row=0, rowspan=2, column=2, pady="30", padx="20")

        boton_calculo = tk.Button(borde_1,
                                  text="Calcular",
                                  **style.STYLE_BUTTON,
                                  )
        boton_calculo.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_calculo.bind('<Enter>', event.on_enter)
        boton_calculo.bind('<Leave>', event.on_leave)

        outputFrame = tk.Frame(self, background=style.BG)
        outputFrame.columnconfigure(0, weight=1)
        outputFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True,)

        # label signo
        tk.Label(outputFrame,
                 text="Signo",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0)

        # label exponente
        tk.Label(outputFrame,
                 text="Exponente",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=0)

        # label mantisa
        tk.Label(outputFrame,
                 text="Mantisa",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=2, column=0)

        # label hexadecimal
        tk.Label(outputFrame,
                 text="Representación\nHexadecimal",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=3, column=0)

        # entry desactivado signo
        self.resultado_signo = tk.StringVar()
        tk.Entry(outputFrame,
                 textvariable=self.resultado_signo,
                 **style.STYLE_ENTRY_DES,
                 ).grid(row=0, column=1, pady="20", padx=(0, 20), sticky=tk.EW)

        # entry desactivado exponente
        self.resultado_exponente = tk.StringVar()
        tk.Entry(outputFrame,
                 textvariable=self.resultado_exponente,
                 **style.STYLE_ENTRY_DES,
                 ).grid(row=1, column=1, pady="20", padx=(0, 20), sticky=tk.EW)

        # entry desactivado mantisa
        self.resultado_mantisa = tk.StringVar()
        tk.Entry(outputFrame,
                 textvariable=self.resultado_mantisa,
                 **style.STYLE_ENTRY_DES,
                 ).grid(row=2, column=1, pady="20", padx=(0, 20), sticky=tk.EW)

        # entry desactivado hexadecimal
        self.resultado_hexadecimal = tk.StringVar()
        tk.Entry(outputFrame,
                 textvariable=self.resultado_hexadecimal,
                 **style.STYLE_ENTRY_DES,
                 ).grid(row=3, column=1, pady="20", padx=(0, 20), sticky=tk.EW)

        # boton para regresar
        borde_2 = tk.LabelFrame(self,
                                **style.STYLE_BUTTON_RETURN_BORDER)
        borde_2.pack(side=tk.BOTTOM, pady=(0, 20))

        boton_return = tk.Button(borde_2,
                                 text="Regresar",
                                 **style.STYLE_BUTTON_RETURN,
                                 command=self.move_to_home
                                 )
        boton_return.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_return.bind('<Enter>', event.on_enter_return)
        boton_return.bind('<Leave>', event.on_leave_return)
