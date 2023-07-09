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
import matplotlib.figure
import numpy as np
import functions.events as event
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from static import style
from functions import funcion_biseccion as biseccion
from validation import validacion


class Biseccion(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(background=style.BG)
        self.init_widgets()

    def validar_campos(self):
        if validacion.validate_number_float(self.valor_a.get()) is True and validacion.validate_number_float(self.valor_b.get()) is True and validacion.validate_number_float(self.valor_c.get()) is True:
            if validacion.validate_number_float(self.valor_intervalo_a.get()) is True and validacion.validate_number_float(self.valor_intervalo_b.get()) is True:
                self.texto_alerta.set("")
                self.calcular()
            else:
                self.texto_alerta.set("Error en el intervalo")
        else:
            self.texto_alerta.set("Error en la ecuación")

    def calcular(self):
        a = float(self.valor_a.get())
        b = float(self.valor_b.get())
        c = float(self.valor_c.get())
        f = lambda x: a*(pow(x, 2)) + b*x + c
        intervalo_a = float(self.valor_intervalo_a.get())
        intervalo_b = float(self.valor_intervalo_b.get())
        respuesta = biseccion.metodo_biseccion(f, intervalo_a, intervalo_b)
        self.respuesta.set(
            respuesta if respuesta is not None else "No se encontró una solución en el intervalo")

    def init_widgets(self):
        tk.Label(self,
                 text="Método de Bisección",
                 **style.STYLE_TITTLE,
                 ).pack(side=tk.TOP, fill=tk.BOTH, pady=30)

        input_frame = tk.Frame(self, background=style.BG)
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)
        input_frame.columnconfigure(2, weight=1)
        input_frame.columnconfigure(3, weight=1)
        input_frame.columnconfigure(4, weight=1)
        input_frame.columnconfigure(5, weight=1)
        input_frame.columnconfigure(6, weight=1)
        input_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        tk.Label(input_frame,
                 text="Ecuación",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0, padx=(20, 40))

        tk.Label(input_frame,
                 text="x**2    +",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=2)

        tk.Label(input_frame,
                 text="x    +",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=4)

        tk.Label(input_frame,
                 text="Intervalo",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=0, padx=20, pady=15)

        tk.Label(input_frame,
                 text="x**2    +",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=2, pady=15)

        tk.Label(input_frame,
                 text=" [ ",
                 **style.STYLE_TITTLE,
                 ).grid(row=1, column=1, pady=15)

        tk.Label(input_frame,
                 text=" : ",
                 **style.STYLE_TITTLE,
                 ).grid(row=1, column=3, pady=15)

        tk.Label(input_frame,
                 text=" ] ",
                 **style.STYLE_TITTLE,
                 ).grid(row=1, column=5, pady=15)

        tk.Label(input_frame,
                 text="Respuesta",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=2, column=0, padx=20, pady=15)

        # entry para el valor a de la ecuaacion
        borde_entry_1 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_1.grid(row=0, column=1, padx=(10, 0))

        self.valor_a = tk.StringVar()
        entry_valor_a = tk.Entry(borde_entry_1,
                                 textvariable=self.valor_a,
                                 **style.STYLE_ENTRY,
                                 width=6,
                                 )
        entry_valor_a.pack(side=tk.TOP, fill=tk.X, expand=True)

        canvas_linea_1 = tk.Canvas(
            borde_entry_1, **style.STYLE_CANVAS, width=50)
        canvas_linea_1.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_1.create_line(0, 0, 50, 0, **style.STYLE_CANVAS_LINE)

        # entry para el valor b de la ecuacion
        borde_entry_2 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_2.grid(row=0, column=3, padx=(10, 0))

        self.valor_b = tk.StringVar()
        entry_valor_b = tk.Entry(borde_entry_2,
                                 textvariable=self.valor_b,
                                 **style.STYLE_ENTRY,
                                 width=6,
                                 )
        entry_valor_b.pack(side=tk.TOP)

        canvas_linea_2 = tk.Canvas(
            borde_entry_2, **style.STYLE_CANVAS, width=50)
        canvas_linea_2.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_2.create_line(0, 0, 50, 0, **style.STYLE_CANVAS_LINE)

        # entry para el valor C de la ecuacion
        borde_entry_3 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_3.grid(row=0, column=5, padx=(10, 0))

        self.valor_c = tk.StringVar()
        entry_valor_c = tk.Entry(borde_entry_3,
                                 textvariable=self.valor_c,
                                 **style.STYLE_ENTRY,
                                 width=6,
                                 )
        entry_valor_c.pack(side=tk.TOP)

        canvas_linea_3 = tk.Canvas(
            borde_entry_3, **style.STYLE_CANVAS, width=50)
        canvas_linea_3.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_3.create_line(0, 0, 50, 0, **style.STYLE_CANVAS_LINE)

        # entry para el valor A del intervalo
        borde_entry_4 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_4.grid(row=1, column=2, padx=(10, 0))

        self.valor_intervalo_a = tk.StringVar()
        entry_valor_intervalo_a = tk.Entry(borde_entry_4,
                                           textvariable=self.valor_intervalo_a,
                                           **style.STYLE_ENTRY,
                                           width=6,
                                           )
        entry_valor_intervalo_a.pack(side=tk.TOP)

        canvas_linea_4 = tk.Canvas(
            borde_entry_4, **style.STYLE_CANVAS, width=50)
        canvas_linea_4.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_4.create_line(0, 0, 50, 0, **style.STYLE_CANVAS_LINE)

        # entry para el valor B del intervalo
        borde_entry_5 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_5.grid(row=1, column=4, padx=(10, 0))

        self.valor_intervalo_b = tk.StringVar()
        entry_valor_intervalo_b = tk.Entry(borde_entry_5,
                                           textvariable=self.valor_intervalo_b,
                                           **style.STYLE_ENTRY,
                                           width=6,
                                           )
        entry_valor_intervalo_b.pack(side=tk.TOP)

        canvas_linea_5 = tk.Canvas(
            borde_entry_5, **style.STYLE_CANVAS, width=50)
        canvas_linea_5.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_5.create_line(0, 0, 50, 0, **style.STYLE_CANVAS_LINE)

        # entry desactivado para la respuesta
        borde_entry_6 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_6.grid(row=2, column=1, columnspan=5)

        self.respuesta = tk.StringVar()
        entry_respuesta = tk.Entry(borde_entry_6,
                                   textvariable=self.respuesta,
                                   **style.STYLE_ENTRY,
                                   )
        entry_respuesta.pack(side=tk.TOP, fill=tk.X, expand=True)

        canvas_linea_6 = tk.Canvas(
            borde_entry_6, **style.STYLE_CANVAS, width=500)
        canvas_linea_6.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_6.create_line(0, 0, 500, 0, **style.STYLE_CANVAS_LINE)

        # boton para calcular
        borde_entry_7 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_7.grid(row=0, rowspan=3, column=6, padx=60)

        borde_1 = tk.LabelFrame(borde_entry_7, **style.STYLE_BUTTON_BORDER)
        borde_1.pack()

        boton_calculo = tk.Button(borde_1,
                                  text="Calcular",
                                  **style.STYLE_BUTTON,
                                  command=self.validar_campos,
                                  )
        boton_calculo.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=0)

        boton_calculo.bind('<Enter>', event.on_enter)
        boton_calculo.bind('<Leave>', event.on_leave)

        # label alerta
        self.texto_alerta = tk.StringVar()
        tk.Label(borde_entry_7,
                 textvariable=self.texto_alerta,
                 **style.STYLE_WARNING
                 ).pack()

        output_frame = tk.Frame(self, background=style.BG)
        output_frame.pack(side=tk.TOP, fill=tk.BOTH,
                          expand=True)

        self.fig = matplotlib.figure.Figure(facecolor=style.BG)
        self.ax = self.fig.add_subplot(facecolor=style.BG)

        self.ax.spines['bottom'].set_color(style.COLOR_AQUA)
        self.ax.spines['bottom'].set_linewidth(2)
        self.ax.spines['left'].set_color(style.COLOR_AQUA)
        self.ax.spines['left'].set_linewidth(2)
        self.ax.spines['right'].set_color(style.COLOR_AQUA)
        self.ax.spines['right'].set_linewidth(2)
        self.ax.spines['top'].set_color(style.COLOR_AQUA)
        self.ax.spines['top'].set_linewidth(2)

        self.ax.tick_params(axis='both', colors=style.COLOR_AQUA,
                            labelsize=10, size=7, width=2)

        self.canvas_figura = FigureCanvasTkAgg(self.fig, master=output_frame)
        self.canvas_figura.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH,
                                                expand=True)