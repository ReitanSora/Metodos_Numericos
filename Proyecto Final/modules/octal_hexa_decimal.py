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


class OctalHexaDecimal(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(background=style.BG)
        self.init_widgets()

    def move_to_home(self):
        self.vaciar_campos()
        self.controller.move_to_home()

    def vaciar_campos(self):
        self.valor_octal.set("")
        self.valor_hexadecimal.set("")
        self.respuesta_odecimal.set("")
        self.respuesta_hdecimal.set("")

    def validacion_calculo_octal(self):
        if validacion.validate_number_octal(self.valor_octal.get()) is True:
            self.texto_alerta_valor_octal.set("")
            self.calcular_octal()
        else:
            self.texto_alerta_valor_octal.set("Ingrese numeros entre 0-7")

    def calcular_octal(self):
        self.respuesta_odecimal.set(sistemas.octal_decimal(int(self.valor_octal.get())))

    def init_widgets(self):
        # label titulo
        tk.Label(self,
                 text="Transformación de Octal a Decimal",
                 **style.STYLE_TITTLE,
                 ).pack(side=tk.TOP, fill=tk.BOTH, pady=30)

        info_frame = tk.Frame(self, background=style.BG)
        info_frame.columnconfigure(0, weight=1)
        info_frame.pack(side=tk.TOP, fill=tk.BOTH)

        # label valor
        tk.Label(info_frame,
                 text="Valor octal",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0, pady=10, sticky=tk.N)

        # label resultado
        tk.Label(info_frame,
                 text="Resultado",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=0)

        # entry valor octal
        borde_entry_1 = tk.LabelFrame(info_frame,
                                      **style.STYLE_ENTRY_BORDER
                                      )
        borde_entry_1.grid(row=0, column=1, pady=(10, 20), sticky=tk.EW)

        self.valor_octal = tk.StringVar()
        tk.Entry(borde_entry_1,
                 textvariable=self.valor_octal,
                 **style.STYLE_ENTRY_NUMBERS,
                 ).pack(fill=tk.BOTH, expand=True)

        # label alerta valor octal
        self.texto_alerta_valor_octal = tk.StringVar()
        tk.Label(borde_entry_1,
                 textvariable=self.texto_alerta_valor_octal,
                 **style.STYLE_WARNING
                 ).pack()

        # entry desactivado respuesta de octal a decimal
        self.respuesta_odecimal = tk.StringVar()
        tk.Entry(info_frame,
                 textvariable=self.respuesta_odecimal,
                 **style.STYLE_ENTRY_DES,
                 ).grid(row=1, column=1, pady=20, sticky=tk.EW)

        # label titulo
        tk.Label(self,
                 text="Transformación de Hexadecimal a Decimal",
                 **style.STYLE_TITTLE,
                 ).pack(side=tk.TOP, fill=tk.BOTH, pady=30)

        info_frame_2 = tk.Frame(self, background=style.BG)
        info_frame_2.columnconfigure(0, weight=1)
        info_frame_2.pack(side=tk.TOP, fill=tk.BOTH)

        # label valor
        tk.Label(info_frame_2,
                 text="Valor hexadecimal",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0, pady=10, sticky=tk.N)

        # label resultado
        tk.Label(info_frame_2,
                 text="Resultado",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=0)

        # entry valor
        borde_entry_2 = tk.LabelFrame(info_frame_2,
                                      **style.STYLE_ENTRY_BORDER
                                      )
        borde_entry_2.grid(row=0, column=1, pady=(10, 20), sticky=tk.EW)

        self.valor_hexadecimal = tk.StringVar()
        tk.Entry(borde_entry_2,
                 textvariable=self.valor_hexadecimal,
                 **style.STYLE_ENTRY_NUMBERS,
                 ).pack(fill=tk.BOTH, expand=True)

        # label alerta valor hexadecimal
        self.texto_alerta_valor_hexadecimal = tk.StringVar()
        tk.Label(borde_entry_2,
                 textvariable=self.texto_alerta_valor_hexadecimal,
                 **style.STYLE_WARNING
                 ).pack()

        # entry desactivado respuesta de hexa a decimal
        self.respuesta_hdecimal = tk.StringVar()
        tk.Entry(info_frame_2,
                 textvariable=self.respuesta_hdecimal,
                 **style.STYLE_ENTRY_DES,
                 ).grid(row=1, column=1, pady=20, sticky=tk.EW)

        # boton para calcular de octal a decimal
        borde_1 = tk.LabelFrame(info_frame,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.grid(row=0, rowspan=2, column=3, pady=30, padx=40)

        boton_calculo_1 = tk.Button(borde_1,
                                    text="Calcular",
                                    **style.STYLE_BUTTON,
                                    command=self.validacion_calculo_octal
                                    )
        boton_calculo_1.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_calculo_1.bind('<Enter>', event.on_enter)
        boton_calculo_1.bind('<Leave>', event.on_leave)

        # boton para calcular de hexa a decimal
        borde_2 = tk.LabelFrame(info_frame_2,
                                **style.STYLE_BUTTON_BORDER)
        borde_2.grid(row=0, rowspan=2, column=3, pady=30, padx=40)

        boton_calculo_2 = tk.Button(borde_2,
                                    text="Calcular",
                                    **style.STYLE_BUTTON,
                                    )
        boton_calculo_2.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_calculo_2.bind('<Enter>', event.on_enter)
        boton_calculo_2.bind('<Leave>', event.on_leave)

        # boton para regresar
        borde_3 = tk.LabelFrame(self,
                                **style.STYLE_BUTTON_RETURN_BORDER)
        borde_3.pack(side=tk.BOTTOM, pady=(0, 20))

        boton_return = tk.Button(borde_3,
                                 text="Regresar",
                                 **style.STYLE_BUTTON_RETURN,
                                 command=self.move_to_home
                                 )
        boton_return.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_return.bind('<Enter>', event.on_enter_return)
        boton_return.bind('<Leave>', event.on_leave_return)
