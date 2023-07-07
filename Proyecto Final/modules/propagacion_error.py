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
from functions import funcion_propagacion as propagacion
from validation import validacion


class PropErrores(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG)
        self.controller = controller
        self.init_widgets()

    def move_to_home(self):
        self.controller.move_to_home()

    def validar_campo(self):
        if validacion.validate_number_float(self.exponente.get()) is True:
            self.calcular()

    def calcular(self):
        self.respuesta.set(propagacion.propagacion_errores(float(self.exponente.get())))

    def init_widgets(self):
        tk.Label(self,
                 text="Propagación de Errores",
                 **style.STYLE_TITTLE,
                 ).pack(side=tk.TOP, fill=tk.BOTH, pady=30)

        inputFrame = tk.Frame(self, background=style.BG)
        inputFrame.columnconfigure(0, weight=1)
        inputFrame.pack(side=tk.TOP, fill=tk.BOTH)

        # label ecuacion
        tk.Label(inputFrame,
                 text="Ecuación",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0)

        # label exponente
        tk.Label(inputFrame,
                 text="Exponente",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=0)

        # label respuesta
        tk.Label(inputFrame,
                 text="Respuesta",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=2, column=0)

        # label ecuacion usada
        tk.Label(inputFrame,
                 text="(e^x)/(e^x)-1",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=1, pady="10", padx="20")

        # entry desactivado respuesta
        self.respuesta = tk.StringVar()
        tk.Entry(inputFrame,
                 textvariable=self.respuesta,
                 **style.STYLE_ENTRY_DES,
                 ).grid(row=2, column=1, pady="10", padx="20")

        # entry exponente
        self.exponente = tk.StringVar()
        tk.Entry(inputFrame,
                 textvariable=self.exponente,
                 **style.STYLE_ENTRY,
                 ).grid(row=1, column=1, pady="10", padx="20", sticky=tk.EW)

        # boton para calcular
        borde_1 = tk.LabelFrame(inputFrame,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.grid(row=0, rowspan=3, column=2, pady="30", padx="20")

        boton_calculo = tk.Button(borde_1,
                                  text="Calcular",
                                  **style.STYLE_BUTTON,
                                  command=self.validar_campo
                                  )
        boton_calculo.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_calculo.bind('<Enter>', event.on_enter)
        boton_calculo.bind('<Leave>', event.on_leave)

        outputFrame = tk.Frame(self, background="#666666")
        outputFrame.pack(side=tk.TOP, fill=tk.BOTH,
                         expand=True, padx="10", pady="10")

        # boton para regresar
        borde_2 = tk.LabelFrame(self,
                                **style.STYLE_BUTTON_RETURN_BORDER)
        borde_2.pack(side=tk.TOP, padx="10", pady="10")

        boton_return = tk.Button(borde_2,
                                 text="Regresar",
                                 **style.STYLE_BUTTON_RETURN,
                                 command=self.move_to_home
                                 )
        boton_return.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_return.bind('<Enter>', event.on_enter_return)
        boton_return.bind('<Leave>', event.on_leave_return)