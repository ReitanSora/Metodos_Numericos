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
from static import style
from validation import validacion
import functions.events as event
import functions.funcion_errores as error


class Errores(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(background=style.BG)
        self.init_widgets()

    def move(self):
        self.vaciar_campos()
        self.controller.move_to_home()

    def vaciar_campos(self):
        self.valor_decimal.set("")
        self.valor_aproximado.set("")
        self.respuesta_error_abs.set("")
        self.respuesta_error_rel.set("")
        self.texto_alerta_valor_decimal.set("")

    def validacion_campos(self):
        try:
            if validacion.validate_decimal(self.valor_decimal.get()) is True:
                self.texto_alerta_valor_decimal.set("")
                self.calculo_errores()
            else:
                self.texto_alerta_valor_decimal.set(
                    "Ingrese un valor decimal con punto")
        except (SyntaxError, ValueError):
            self.texto_alerta_valor_decimal.set(
                "Ingrese un valor decimal con punto")

    def calculo_errores(self):
        valor_aproximado, error_absoluto, error_relativo = error.calculo_errores(
            float(self.valor_decimal.get()))
        self.valor_aproximado.set(str(valor_aproximado))
        self.respuesta_error_abs.set(str(error_absoluto))
        self.respuesta_error_rel.set(str(error_relativo))

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
                 text="Valor decimal",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0, pady=10, sticky=tk.N)

        # label exponente
        tk.Label(inputFrame,
                 text="Valor aproximado",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=0)

        # label respuesta
        tk.Label(inputFrame,
                 text="Error absoluto",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=3, column=0)

        # label respuesta
        tk.Label(inputFrame,
                 text="Error relativo",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=4, column=0)

        # label informacion
        tk.Label(inputFrame,
                 text="Calculo de errores entre el valor ingresado y el aproximado",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=2, column=0, columnspan=4, pady=20)

        # entry valor decimal
        borde_entry_1 = tk.LabelFrame(inputFrame,
                                      **style.STYLE_ENTRY_BORDER
                                      )
        borde_entry_1.grid(row=0, column=1, pady=(10, 20), sticky=tk.EW)

        self.valor_decimal = tk.StringVar()
        tk.Entry(borde_entry_1,
                 textvariable=self.valor_decimal,
                 **style.STYLE_ENTRY_NUMBERS,
                 ).pack(fill=tk.BOTH, expand=True)

        # label alerta valor decimal
        self.texto_alerta_valor_decimal = tk.StringVar()
        tk.Label(borde_entry_1,
                 textvariable=self.texto_alerta_valor_decimal,
                 **style.STYLE_WARNING
                 ).pack()

        # entry desactivado valor aproximado
        self.valor_aproximado = tk.StringVar()
        tk.Entry(inputFrame,
                 textvariable=self.valor_aproximado,
                 **style.STYLE_ENTRY_DES,
                 ).grid(row=1, column=1, pady=20, sticky=tk.EW)

        # entry desactivado respuesta
        self.respuesta_error_abs = tk.StringVar()
        tk.Entry(inputFrame,
                 textvariable=self.respuesta_error_abs,
                 **style.STYLE_ENTRY_DES,
                 ).grid(row=3, column=1, columnspan=2, pady=30, sticky=tk.EW)

        # entry desactivado respuesta
        self.respuesta_error_rel = tk.StringVar()
        tk.Entry(inputFrame,
                 textvariable=self.respuesta_error_rel,
                 **style.STYLE_ENTRY_DES,
                 ).grid(row=4, column=1, columnspan=2, pady=30, sticky=tk.EW)

        # boton para calcular
        borde_1 = tk.LabelFrame(inputFrame,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.grid(row=0, rowspan=2, column=3, pady="30", padx="20")

        boton_calculo = tk.Button(borde_1,
                                  text="Calcular",
                                  **style.STYLE_BUTTON,
                                  command=self.validacion_campos
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
