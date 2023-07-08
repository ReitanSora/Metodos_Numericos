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
        if validacion.validate_number_float(self.valor_decimal.get()) is True:
            self.texto_alerta_valor_decimal.set("")
            self.calculo_errores()
        else:
            self.texto_alerta_valor_decimal.set("Números 0-9 y '.'")

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

        input_frame = tk.Frame(self, background=style.BG)
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)
        input_frame.columnconfigure(2, weight=1)
        input_frame.pack(side=tk.TOP, fill=tk.BOTH)

        # label ecuacion
        tk.Label(input_frame,
                 text="Valor decimal",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0, pady=10, sticky=tk.N)

        # label exponente
        tk.Label(input_frame,
                 text="Valor aproximado",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=0)

        # label respuesta
        tk.Label(input_frame,
                 text="Error absoluto",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=3, column=0)

        # label respuesta
        tk.Label(input_frame,
                 text="Error relativo",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=4, column=0)

        # label informacion
        tk.Label(input_frame,
                 text="○ Calculo de errores entre el valor ingresado y el aproximado",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=2, column=0, columnspan=2, pady=20)

        # entry valor decimal
        borde_entry_1 = tk.LabelFrame(input_frame,
                                      **style.STYLE_ENTRY_BORDER
                                      )
        borde_entry_1.grid(row=0, column=1, pady=(10, 20), sticky=tk.EW)

        self.valor_decimal = tk.StringVar()
        tk.Entry(borde_entry_1,
                 textvariable=self.valor_decimal,
                 **style.STYLE_ENTRY,
                 ).pack(fill=tk.BOTH, expand=True)
        
        canvas_linea_1 = tk.Canvas(
            borde_entry_1, **style.STYLE_CANVAS, width=250)
        canvas_linea_1.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_1.create_line(0, 0, 250, 0, **style.STYLE_CANVAS_LINE)

        # label alerta valor decimal
        self.texto_alerta_valor_decimal = tk.StringVar()
        tk.Label(borde_entry_1,
                 textvariable=self.texto_alerta_valor_decimal,
                 **style.STYLE_WARNING
                 ).pack()

        # entry desactivado valor aproximado
        borde_entry_2 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_2.grid(row=1, column=1, pady=20, sticky=tk.EW)

        self.valor_aproximado = tk.StringVar()
        tk.Entry(borde_entry_2,
                 textvariable=self.valor_aproximado,
                 **style.STYLE_ENTRY_DES,
                 ).pack()
        
        canvas_linea_2 = tk.Canvas(
            borde_entry_2, **style.STYLE_CANVAS, width=250)
        canvas_linea_2.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_2.create_line(0, 0, 250, 0, **style.STYLE_CANVAS_LINE)

        # entry desactivado respuesta
        borde_entry_3 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_3.grid(row=3, column=1, pady=30, sticky=tk.EW)

        self.respuesta_error_abs = tk.StringVar()
        tk.Entry(borde_entry_3,
                 textvariable=self.respuesta_error_abs,
                 **style.STYLE_ENTRY_DES,
                 ).pack()
        
        canvas_linea_3 = tk.Canvas(
            borde_entry_3, **style.STYLE_CANVAS, width=250)
        canvas_linea_3.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_3.create_line(0, 0, 250, 0, **style.STYLE_CANVAS_LINE)

        # entry desactivado respuesta
        borde_entry_4 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_4.grid(row=4, column=1, pady=30, sticky=tk.EW)

        self.respuesta_error_rel = tk.StringVar()
        tk.Entry(borde_entry_4,
                 textvariable=self.respuesta_error_rel,
                 **style.STYLE_ENTRY_DES,
                 ).pack()
        
        canvas_linea_4 = tk.Canvas(
            borde_entry_4, **style.STYLE_CANVAS, width=250)
        canvas_linea_4.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_4.create_line(0, 0, 250, 0, **style.STYLE_CANVAS_LINE)

        # boton para calcular
        borde_1 = tk.LabelFrame(input_frame,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.grid(row=0, rowspan=2, column=2, pady=30, padx=20)

        boton_calculo = tk.Button(borde_1,
                                  text="Calcular",
                                  **style.STYLE_BUTTON,
                                  command=self.validacion_campos
                                  )
        boton_calculo.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_calculo.bind('<Enter>', event.on_enter)
        boton_calculo.bind('<Leave>', event.on_leave)
