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


class BinarioDecimal(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(background=style.BG)
        self.init_widgets()

    def move_to_home(self):
        self.controller.move_to_home()

    def init_widgets(self):
        # label titulo
        tk.Label(self,
                 text="Transformación de Binario a Decimal",
                 **style.STYLE_TITTLE,
                 ).pack(side=tk.TOP, fill=tk.BOTH, pady=30)

        info_frame = tk.Frame(self, background=style.BG)
        info_frame.columnconfigure(0, weight=1)
        info_frame.pack(side=tk.TOP, fill=tk.BOTH)

        # label ecuacion
        tk.Label(info_frame,
                 text="Valor",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0)

        # label exponente
        tk.Label(info_frame,
                 text="Resultado",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=0)

        # entry valor
        self.valor_binario = tk.StringVar()
        tk.Entry(info_frame,
                 textvariable=self.valor_binario,
                 **style.STYLE_ENTRY_SCREENS,
                 ).grid(row=0, column=1, pady=(10, 20), padx="20", sticky=tk.EW)

        # entry desactivado respuesta
        self.respuesta_decimal = tk.StringVar()
        tk.Entry(info_frame,
                 textvariable=self.respuesta_decimal,
                 **style.STYLE_ENTRY_SCREENS_DES,
                 ).grid(row=1, column=1, pady=(20, 20), padx="20", sticky=tk.EW)

        # label titulo
        tk.Label(self,
                 text="Transformación de Decimal a Binario",
                 **style.STYLE_TITTLE,
                 ).pack(side=tk.TOP, fill=tk.BOTH, pady=30)

        info_frame_2 = tk.Frame(self, background=style.BG)
        info_frame_2.columnconfigure(0, weight=1)
        info_frame_2.pack(side=tk.TOP, fill=tk.BOTH)

        # label ecuacion
        tk.Label(info_frame_2,
                 text="Valor",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0)

        # label exponente
        tk.Label(info_frame_2,
                 text="Resultado",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=0)

        # entry valor
        self.valor_decimal = tk.StringVar()
        tk.Entry(info_frame_2,
                 textvariable=self.valor_decimal,
                 **style.STYLE_ENTRY_SCREENS,
                 ).grid(row=0, column=1, pady=(10, 20), padx="20", sticky=tk.EW)

        # entry desactivado respuesta
        self.respuesta_binario = tk.StringVar()
        tk.Entry(info_frame_2,
                 textvariable=self.respuesta_binario,
                 **style.STYLE_ENTRY_SCREENS_DES,
                 ).grid(row=1, column=1, pady=(20, 20), padx="20", sticky=tk.EW)

        # boton para calcular de binario a decimal
        borde_1 = tk.LabelFrame(info_frame,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.grid(row=0, rowspan=2, column=3, pady="30", padx="20")

        boton_calculo_1 = tk.Button(borde_1,
                                    text="Calcular",
                                    **style.STYLE_BUTTON,
                                    )
        boton_calculo_1.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_calculo_1.bind('<Enter>', event.on_enter)
        boton_calculo_1.bind('<Leave>', event.on_leave)

        # boton para calcular de decimal a binario
        borde_2 = tk.LabelFrame(info_frame_2,
                                **style.STYLE_BUTTON_BORDER)
        borde_2.grid(row=0, rowspan=2, column=3, pady="30", padx="20")

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
