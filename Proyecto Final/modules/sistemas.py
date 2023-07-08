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
import functions.funcion_sistemas_numeracion as sistemas
from static import style
from validation import validacion


class Conversiones(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(background=style.BG)
        self.conversion = tk.IntVar(value=1)
        self.init_widgets()

    def move_to_home(self):
        self.vaciar_campos()
        self.controller.move_to_home()

    def vaciar_campos(self):
        self.valor_original.set("")
        self.respuesta.set("")
        self.texto_alerta_valor_original.set("")

    def validacion_calculo(self):
        if self.conversion.get() == 1:
            if validacion.validate_number_binary(self.valor_original.get()) is True:
                self.texto_alerta_valor_original.set("")
                self.calcular_binario_a_decimal()
            else:
                self.texto_alerta_valor_original.set(
                    "Ingrese un valor correcto")
        elif self.conversion.get() == 2:
            if validacion.validate_number_octal(self.valor_original.get()) is True:
                self.texto_alerta_valor_original.set("")
                self.calcular_octal()
            else:
                self.texto_alerta_valor_original.set(
                    "Ingrese un valor correcto")
        elif self.conversion.get() == 3:
            if validacion.validate_number_decimal(self.valor_original.get()) is True:
                self.texto_alerta_valor_original.set("")
                self.calcular_hexadecimal()
            else:
                self.texto_alerta_valor_original.set(
                    "Ingrese un valor correcto")
        elif self.conversion.get() == 4:
            if validacion.validate_number_decimal(self.valor_original.get()) is True:
                self.texto_alerta_valor_original.set("")
                self.calcular_decimal_a_binario()
            else:
                self.texto_alerta_valor_original.set(
                    "Ingrese un valor correcto")
        elif self.conversion.get() == 5:
            if validacion.validate_number_decimal(self.valor_original.get()) is True:
                self.texto_alerta_valor_original.set("")
                self.calcular_decimal_a_octal()
            else:
                self.texto_alerta_valor_original.set(
                    "Ingrese un valor correcto")
        elif self.conversion.get() == 6:
            if validacion.validate_number_decimal(self.valor_original.get()) is True:
                self.texto_alerta_valor_original.set("")
                self.calcular_decimal_a_hexa()
            else:
                self.texto_alerta_valor_original.set(
                    "Ingrese un valor correcto")

    def calcular_binario_a_decimal(self):
        self.respuesta.set(sistemas.binario_decimal(
            int(self.valor_original.get())))

    def calcular_octal(self):
        self.respuesta.set(sistemas.octal_decimal(
            int(self.valor_original.get())))

    def calcular_hexadecimal(self):
        self.respuesta.set(sistemas.hexa_decimal(self.valor_original.get()))

    def calcular_decimal_a_binario(self):
        self.respuesta.set(sistemas.decimal_binario(
            int(self.valor_original.get())))

    def calcular_decimal_a_octal(self):
        self.respuesta.set(sistemas.decimal_octal(
            int(self.valor_original.get())))

    def calcular_decimal_a_hexa(self):
        self.respuesta.set(sistemas.decimal_hexa(
            int(self.valor_original.get())))

    def init_widgets(self):
        # label titulo
        tk.Label(self,
                 text="Transformación de Binario a Decimal",
                 **style.STYLE_TITTLE,
                 ).pack(side=tk.TOP, fill=tk.BOTH, pady=30)

        info_frame = tk.Frame(self, background=style.BG)
        info_frame.columnconfigure(0, weight=1)
        info_frame.columnconfigure(1, weight=1)
        info_frame.columnconfigure(2, weight=1)
        info_frame.pack(side=tk.TOP, fill=tk.BOTH)

        # label valor
        tk.Label(info_frame,
                 text="Valor",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0, pady=10, sticky=tk.N)

        # label conversion
        tk.Label(info_frame,
                 text="Conversión",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=0, pady=10, sticky=tk.N)

        # label resultado
        tk.Label(info_frame,
                 text="Resultado",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=3, column=0, pady=10, sticky=tk.N)

        # entry valor binario
        borde_entry_1 = tk.LabelFrame(info_frame,
                                      **style.STYLE_ENTRY_BORDER
                                      )
        borde_entry_1.grid(row=0, column=1, columnspan=2,
                           pady=(10, 20), sticky=tk.EW)

        self.valor_original = tk.StringVar()
        tk.Entry(borde_entry_1,
                 textvariable=self.valor_original,
                 **style.STYLE_ENTRY,
                 ).pack(side=tk.TOP, expand=True)

        canvas_linea_1 = tk.Canvas(
            borde_entry_1, **style.STYLE_CANVAS, width=250)
        canvas_linea_1.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_1.create_line(0, 0, 250, 0, **style.STYLE_CANVAS_LINE)

        # label alerta valor binario
        self.texto_alerta_valor_original = tk.StringVar()
        tk.Label(borde_entry_1,
                 textvariable=self.texto_alerta_valor_original,
                 **style.STYLE_WARNING
                 ).pack()

        # entry desactivado respuesta
        borde_entry_2 = tk.LabelFrame(info_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_2.grid(row=3, column=1, columnspan=2,
                           pady=(20, 20), sticky=tk.EW)

        self.respuesta = tk.StringVar()
        tk.Entry(borde_entry_2,
                 textvariable=self.respuesta,
                 **style.STYLE_ENTRY_DES,
                 ).pack(side=tk.TOP, expand=True)

        canvas_linea_2 = tk.Canvas(
            borde_entry_2, **style.STYLE_CANVAS, width=250)
        canvas_linea_2.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_2.create_line(0, 0, 250, 0, **style.STYLE_CANVAS_LINE)

        # boton para calcular de binario a decimal
        borde_1 = tk.LabelFrame(info_frame,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.grid(row=0, rowspan=2, column=4, pady=30, padx=20)

        boton_calculo_1 = tk.Button(borde_1,
                                    text="Calcular",
                                    **style.STYLE_BUTTON,
                                    command=self.validacion_calculo
                                    )
        boton_calculo_1.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_calculo_1.bind('<Enter>', event.on_enter)
        boton_calculo_1.bind('<Leave>', event.on_leave)

        CONVERSION_1 = {
            "Binario": 1,
            "Octal": 2,
            "Hexa": 3,
        }

        CONVERSION_2 = {
            "Binario": 4,
            "Octal": 5,
            "Hexa": 6
        }

        borde_seleccion_1 = tk.LabelFrame(
            info_frame, text="N a Decimal", **style.STYLE_ENTRY_BORDER)
        borde_seleccion_1.grid(
            row=1, column=1, columnspan=2, pady=10, sticky=tk.NSEW)

        for keys, values in CONVERSION_1.items():
            tk.Radiobutton(borde_seleccion_1,
                           text=keys,
                           value=values,
                           variable=self.conversion,
                           **style.STYLE_RADIO_BUTTON,
                           ).pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=5)

        borde_seleccion_2 = tk.LabelFrame(
            info_frame, text="Decimal a N", **style.STYLE_ENTRY_BORDER)
        borde_seleccion_2.grid(
            row=2, column=1, columnspan=2, pady=10, sticky=tk.NSEW)

        for keys, values in CONVERSION_2.items():
            tk.Radiobutton(borde_seleccion_2,
                           text=keys,
                           value=values,
                           variable=self.conversion,
                           **style.STYLE_RADIO_BUTTON,
                           ).pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=5)
